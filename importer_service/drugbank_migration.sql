CREATE TABLE public.all_drugs_info (
    name text,
    cas text,
    gene_target_ids_array text[],
    smiles_code text,
    inchi_code text,
    inchi_key text,
    molecular_formula text,
    atc_code text[],
    drugbank_version text
);

CREATE TABLE public.all_genes (
    name text,
    gene_id text,
    drugs_ids text[],
    drugbank_version text
);


CREATE TABLE public.drug_results (
    max_modularity text,
    candidates_number text,
    candidates_validated_number text,
    resolution text,
    drugbank_version text,
    candidates text[],
    candidates_validated text[]
);

CREATE TABLE public.drugs_resolution (
    name text,
    drugbank_version text,
    resolution text,
    modularity_class text
);

CREATE TABLE diseaseAttributes (
  diseaseNID smallint NOT NULL,
  diseaseId varchar(255) NOT NULL,
  diseaseName varchar(255) NOT NULL,
  type varchar(255) NOT NULL,
  PRIMARY KEY (diseaseNID)
);

CREATE TABLE diseaseClass (
  diseaseClassNID smallint NOT NULL,
  vocabulary varchar(255) NOT NULL,
  diseaseClass varchar(255) NOT NULL,
  diseaseClassName varchar(255) NOT NULL,
  PRIMARY KEY (diseaseClassNID)
);

CREATE TABLE disease2class (
  diseaseNID smallint NOT NULL,
  diseaseClassNID smallint NOT NULL,
  PRIMARY KEY (diseaseNID, diseaseClassNID)
);

CREATE TABLE geneAttributes (
  geneNID smallint NOT NULL,
  geneId int DEFAULT NULL,
  geneName varchar(255) DEFAULT NULL,
  geneDescription varchar(255) DEFAULT NULL,
  pLI double precision NULL,
  DSI double precision NULL,
  DPI double precision NULL,
  PRIMARY KEY (geneNID)
);

CREATE TABLE geneDiseaseNetwork (
  NID serial PRIMARY KEY,
  diseaseNID smallint NOT NULL,
  geneNID smallint NOT NULL,
  source varchar(255) DEFAULT NULL,
  association integer NULL,
  associationType text DEFAULT NULL,
  sentence text DEFAULT NULL,
  pmid int DEFAULT NULL,
  score double precision DEFAULT NULL,
  EL varchar(255) DEFAULT NULL,
  EI double precision DEFAULT NULL,
  year int DEFAULT NULL
);

CREATE TABLE variantAttributes (
  variantNID smallint NOT NULL,
  variantId varchar(255) NOT NULL,
  class varchar(255) DEFAULT NULL,
  chromosome varchar(255) DEFAULT NULL,
  coord varchar(255) DEFAULT NULL,
  most_severe_consequence varchar(255) DEFAULT NULL,
  DSI double precision NULL,
  DPI double precision NULL,
  PRIMARY KEY (variantNID)
);

CREATE TABLE variantGene (
  geneNID smallint NOT NULL,
  variantNID smallint NOT NULL,
  PRIMARY KEY (geneNID, variantNID)
);

CREATE TABLE variantDiseaseNetwork (
  NID serial PRIMARY KEY,
  diseaseNID smallint NOT NULL,
  variantNID smallint NOT NULL,
  source varchar(255) DEFAULT NULL,
  association integer DEFAULT NULL,
  associationType text DEFAULT NULL,
  sentence text DEFAULT NULL,
  pmid int DEFAULT NULL,
  score double precision DEFAULT NULL,
  EI double precision DEFAULT NULL,
  year int DEFAULT NULL
);

CREATE INDEX diseaseAttributes_diseaseId ON diseaseAttributes (diseaseId);
CREATE INDEX geneDiseaseNetwork_gd ON geneDiseaseNetwork (diseaseNID,geneNID);
CREATE INDEX geneDiseaseNetwork_geneNID ON geneDiseaseNetwork (geneNID);
CREATE INDEX geneDiseaseNetwork_diseaseNID ON geneDiseaseNetwork (diseaseNID);
CREATE INDEX geneDiseaseNetwork_source ON geneDiseaseNetwork (source);
CREATE INDEX geneAttributes_geneId ON geneAttributes (geneId);
CREATE INDEX variantDiseaseNetwork_vd ON variantDiseaseNetwork (diseaseNID,variantNID);
CREATE INDEX variantDiseaseNetwork_variantNID ON variantDiseaseNetwork (variantNID);
CREATE INDEX variantDiseaseNetwork_diseaseNID ON variantDiseaseNetwork (diseaseNID);
CREATE INDEX variantDiseaseNetwork_source ON variantDiseaseNetwork (source);
CREATE INDEX variantAttributes_variantId ON variantAttributes (variantId);