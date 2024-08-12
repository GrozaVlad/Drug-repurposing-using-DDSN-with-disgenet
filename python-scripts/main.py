import networkx as nx
import psycopg2 as psycopg2
import pandas as pd
from networkx.algorithms import bipartite, community

conn = psycopg2.connect(
    host="localhost",
    database="drugbank",
    user="drugbank",
    password="drugbank",
    port=5433)

cursor = conn.cursor()
cursor.execute("""SELECT final.drug_name,
		final.diseasename,
		final.associationtype,
		final.name as gene_name,
		e.cas,
		e.smiles_code,
		e.inchi_code,
		e.inchi_key,
		e.molecular_formula FROM(
SELECT
-- *
	D.NAME,
	UNNEST(D.DRUGS_IDS) AS DRUG_NAME,
	C.DISEASENAME,
	A.ASSOCIATIONTYPE,
	C.TYPE
    FROM PUBLIC.GENEDISEASENETWORK AS A
    LEFT JOIN PUBLIC.GENEATTRIBUTES AS B ON A.GENENID = B.GENENID
    LEFT JOIN PUBLIC.DISEASEATTRIBUTES AS C ON A.DISEASENID = C.DISEASENID
    LEFT JOIN PUBLIC.ALL_GENES AS D ON B.GENENAME=D.NAME
    WHERE D.DRUGBANK_VERSION='5.1.10' AND A.ASSOCIATIONTYPE IN ('AlteredExpression','Therapeutic','Biomarker','GeneticVariation')
    AND C.TYPE = 'disease'
    AND A.EL IN ('definitive','moderate','strong')
    ORDER BY NID ASC
	) as final
	LEFT JOIN public.all_drugs_info as E on final.drug_name=e.name
	WHERE E.drugbank_version='5.1.10' AND cardinality(E.gene_target_ids_array)!=0
 --LIMIT 100""")

drug_disease_df = pd.DataFrame(drug_disease_associations)
distinct_drugs = drug_disease_df[0].unique()
distinct_diseases = drug_disease_df[1].unique()

edges = [(row[0], row[1]) for row in drug_disease_df.itertuples(index=False)]
print(edges)

# Creating the bipartite graph
B = nx.Graph()

# Adding nodes with the bipartite attribute
B.add_nodes_from(distinct_drugs, bipartite=0)  # drug nodes
B.add_nodes_from(distinct_diseases, bipartite=1)  # disease nodes
B.add_edges_from(edges)

# Projecting the bipartite graph to the drug nodes
G = bipartite.weighted_projected_graph(B, list(range(0, len(drug_nodes))),ratio=False)
nx.write_gexf(G, "./test_project_drugs_weighted_projection_5.1.10.gexf")

