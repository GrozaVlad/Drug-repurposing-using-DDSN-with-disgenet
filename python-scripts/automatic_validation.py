from Bio import Entrez, Medline
import csv

# -------------------------------------------------------------------------
# 1. Configure the list of drugs
# -------------------------------------------------------------------------

# community 1
# drug_list = [
#     'Insulin human', 'Botulinum toxin type B', 'Insulin lispro', 'Insulin glargine',
#     'Insulin glulisine', 'Insulin pork', 'Pyridoxal phosphate', 'Ascorbic acid',
#     'Glutamic acid', 'Glycine', 'Sildenafil', 'Isradipine', 'Pimecrolimus',
#     'Amlodipine', 'Carisoprodol', 'Lindane', 'Atropine', 'Verapamil', 'Loperamide',
#     'Levamisole', 'Sirolimus', 'Ethanol', 'Azathioprine', 'Felodipine', 'Nitrendipine',
#     'Flumazenil', 'Bepridil', 'Mecasermin', 'Insulin detemir', 'Insulin aspart',
#     'Everolimus', 'Zinc', 'Propanoic acid', 'Eflornithine', 'Temsirolimus', 'Teprotumumab',
#     'Insulin beef', 'Somatrem', 'Ubidecarenone', 'Zinc sulfate', 'Insulin degludec',
#     'Calcium Phosphate', 'Artenimol', 'Fostamatinib', 'Brigatinib', 'Fluciclovine (18F)',
#     'Bioallethrin', 'Zinc acetate', 'Zinc chloride', 'Mecasermin rinfabate', 'Insulin human',
#     'Botulinum toxin type B', 'Insulin lispro', 'Insulin glargine', 'Insulin pork',
#     'Pyridoxal phosphate', 'Ascorbic acid', 'Glutamic acid', 'Glycine', 'Sildenafil',
#     'Isradipine', 'Pimecrolimus', 'Carisoprodol', 'Amlodipine', 'Lindane', 'Atropine',
#     'Verapamil', 'Loperamide', 'Levamisole', 'Sirolimus', 'Ethanol', 'Azathioprine',
#     'Felodipine', 'Nitrendipine', 'Flumazenil', 'Bepridil', 'Mecasermin', 'Insulin aspart',
#     'Insulin detemir', 'Insulin glulisine', 'Everolimus', 'Zinc', 'Propanoic acid',
#     'Eflornithine', 'Temsirolimus', 'Teprotumumab', 'Somatrem', 'Ubidecarenone',
#     'Zinc sulfate', 'Insulin beef', 'Insulin degludec', 'Calcium Phosphate', 'Artenimol',
#     'Fostamatinib', 'Brigatinib', 'Fluciclovine (18F)', 'Bioallethrin', 'Zinc acetate',
#     'Zinc chloride', 'Mecasermin rinfabate'
# ]

# community 2
# drug_list = ['Cetuximab', 'Etanercept', 'Collagenase clostridium histolyticum', 'Gemtuzumab ozogamicin', 'Alemtuzumab', 'Alefacept', 'Palivizumab', 'Bevacizumab', 'Glutathione', 'Diethylstilbestrol', 'Porfimer sodium', 'Deferoxamine', 'Tetracycline', 'Dopamine', 'Cinacalcet', 'Minocycline', 'Isoprenaline', 'Eculizumab', 'Vorinostat', 'Nicotinamide', 'Ribostamycin', 'Benzoic acid', 'Ezogabine', 'Migalastat', 'Ethanolamine oleate', 'Dimercaprol', 'Ocriplasmin', 'Stiripentol', 'Florbetaben (18F)', 'Florbetapir (18F)', 'Flutemetamol (18F)', 'Ravulizumab', 'Tafamidis', 'Sarilumab', 'Benralizumab', 'Aducanumab', 'Etelcalcetide', 'Aluminium phosphate', 'Sutimlimab', 'Volanesorsen', 'Pralsetinib', 'Pegcetacoplan', 'Cetuximab', 'Etanercept', 'Collagenase clostridium histolyticum', 'Gemtuzumab ozogamicin', 'Alemtuzumab', 'Alefacept', 'Palivizumab', 'Bevacizumab', 'Glutathione', 'Diethylstilbestrol', 'Ocriplasmin', 'Porfimer sodium', 'Deferoxamine', 'Tetracycline', 'Dopamine', 'Cinacalcet', 'Minocycline', 'Isoprenaline', 'Eculizumab', 'Vorinostat', 'Nicotinamide', 'Ribostamycin', 'Benzoic acid', 'Migalastat', 'Ezogabine', 'Ethanolamine oleate', 'Dimercaprol', 'Stiripentol', 'Florbetaben (18F)', 'Florbetapir (18F)', 'Flutemetamol (18F)', 'Ravulizumab', 'Tafamidis', 'Sarilumab', 'Aducanumab', 'Benralizumab', 'Etelcalcetide', 'Aluminium phosphate', 'Volanesorsen', 'Sutimlimab', 'Pralsetinib', 'Pegcetacoplan']

# community 3
# drug_list = ['Fluvoxamine', 'Erythromycin', 'Glimepiride', 'Phenytoin', 'Amsacrine', 'Terfenadine', 'Trimethadione', 'Acetohexamide', 'Loratadine', 'Imipramine', 'Fluoxetine', 'Chlorpromazine', 'Mephenytoin', 'Ciprofloxacin', 'Hydroxyzine', 'Cinnarizine', 'Levocarnitine', 'Ethosuximide', 'Cisapride', 'Fluphenazine', 'Astemizole', 'Chlorpropamide', 'Tamoxifen', 'Thioridazine', 'Clodronic acid', 'Nateglinide', 'Riluzole', 'Prilocaine', 'Ethotoin', 'Trifluoperazine', 'Perphenazine', 'Benzonatate', 'Repaglinide', 'Phenformin', 'Ketoconazole', 'Melatonin', 'Glipizide', 'Promethazine', 'Etidronic acid', 'Pimozide', 'Gliclazide', 'Tolbutamide', 'Doxepin', 'Nefazodone', 'Desipramine', 'Terazosin', 'Clarithromycin', 'Halofantrine', 'Gliquidone', 'Fosphenytoin', 'Glymidine', 'Flunarizine', 'Methsuximide', 'Sertindole', 'Calcium citrate', 'Pentoxyverine', 'Chlorobutanol', 'Isavuconazole', 'Pitolisant', 'Propiverine', 'Calcium levulinate', 'Acetohexamide', 'Fluvoxamine', 'Erythromycin', 'Glimepiride', 'Phenytoin', 'Amsacrine', 'Terfenadine', 'Trimethadione', 'Loratadine', 'Imipramine', 'Fluoxetine', 'Chlorpromazine', 'Mephenytoin', 'Ciprofloxacin', 'Hydroxyzine', 'Cinnarizine', 'Levocarnitine', 'Ethosuximide', 'Chlorpropamide', 'Cisapride', 'Fluphenazine', 'Astemizole', 'Phenformin', 'Tamoxifen', 'Thioridazine', 'Clodronic acid', 'Nateglinide', 'Riluzole', 'Prilocaine', 'Ethotoin', 'Trifluoperazine', 'Perphenazine', 'Benzonatate', 'Repaglinide', 'Ketoconazole', 'Melatonin', 'Glipizide', 'Promethazine', 'Etidronic acid', 'Pimozide', 'Gliclazide', 'Tolbutamide', 'Doxepin', 'Nefazodone', 'Desipramine', 'Terazosin', 'Clarithromycin', 'Halofantrine', 'Gliquidone', 'Fosphenytoin', 'Glymidine', 'Flunarizine', 'Methsuximide', 'Sertindole', 'Calcium citrate', 'Pentoxyverine', 'Chlorobutanol', 'Isavuconazole', 'Pitolisant', 'Propiverine', 'Calcium levulinate']

# community 4
# drug_list = ['Darbepoetin alfa', 'Erythropoietin', 'Palifermin', 'Cetrorelix', 'Becaplermin', 'Oseltamivir', 'Ampicillin', 'Bosentan', 'Doxapram', 'Gonadorelin', 'Nafarelin', 'Hexachlorophene', 'Heparin', 'Atovaquone', 'Danazol', 'Iron', 'Citric acid', 'Roxadustat', 'Ingenol mebutate', 'Pentaerythritol tetranitrate', 'Lacosamide', 'Sitaxentan', 'Ambrisentan', 'Ganirelix', 'Halcinonide', 'Cholecystokinin', 'Peginesatide', 'Macitentan', 'Methoxy polyethylene glycol-epoetin beta', 'Nitrous acid', 'Aluminum chloride', 'Dibotermin alfa', 'Elagolix', 'Ferrous gluconate', 'Ferrous succinate', 'Ferrous ascorbate', 'Ferrous fumarate', 'Ferrous glycine sulfate', 'Voxelotor', 'Linzagolix', 'Darbepoetin alfa', 'Erythropoietin', 'Palifermin', 'Cetrorelix', 'Becaplermin', 'Oseltamivir', 'Ampicillin', 'Bosentan', 'Doxapram', 'Gonadorelin', 'Nafarelin', 'Hexachlorophene', 'Pentaerythritol tetranitrate', 'Heparin', 'Atovaquone', 'Danazol', 'Iron', 'Citric acid', 'Roxadustat', 'Ingenol mebutate', 'Lacosamide', 'Sitaxentan', 'Ambrisentan', 'Ganirelix', 'Halcinonide', 'Cholecystokinin', 'Peginesatide', 'Macitentan', 'Methoxy polyethylene glycol-epoetin beta', 'Nitrous acid', 'Aluminum chloride', 'Dibotermin alfa', 'Elagolix', 'Ferrous gluconate', 'Ferrous succinate', 'Ferrous ascorbate', 'Ferrous fumarate', 'Ferrous glycine sulfate', 'Voxelotor', 'Linzagolix']

# community 5
# drug_list = ['Flunisolide', 'Medrysone', 'Megestrol acetate', 'Levonorgestrel', 'Progesterone', 'Spironolactone', 'Testosterone', 'Prednisone', 'Fludrocortisone', 'Eplerenone', 'Norethisterone', 'Procaine', 'Mifepristone', 'Rimexolone', 'Fluoxymesterone', 'Drospirenone', 'Ciclesonide', 'Ulipristal', 'Fluticasone furoate', 'Tixocortol', 'Gestrinone', 'Deflazacort', 'Finerenone', 'Flunisolide', 'Medrysone', 'Megestrol acetate', 'Levonorgestrel', 'Progesterone', 'Spironolactone', 'Testosterone', 'Prednisone', 'Fludrocortisone', 'Eplerenone', 'Norethisterone', 'Procaine', 'Mifepristone', 'Rimexolone', 'Fluoxymesterone', 'Drospirenone', 'Ciclesonide', 'Ulipristal', 'Fluticasone furoate', 'Tixocortol', 'Gestrinone', 'Deflazacort', 'Finerenone']

# community 6
# drug_list = ['Caffeine', 'Mesalazine', 'Triamterene', 'Chloramphenicol', 'Amiloride', 'Bumetanide', 'Didanosine', 'Dipyridamole', 'Auranofin', 'Glyburide', 'Sulfinpyrazone', 'Dantrolene', 'Crofelemer', 'Acetylcysteine', 'Ivacaftor', 'Tetracaine', 'Lumacaftor', 'Tezacaftor', 'Abrocitinib', 'Elexacaftor', 'Caffeine', 'Mesalazine', 'Triamterene', 'Chloramphenicol', 'Amiloride', 'Bumetanide', 'Didanosine', 'Dipyridamole', 'Auranofin', 'Glyburide', 'Sulfinpyrazone', 'Dantrolene', 'Crofelemer', 'Acetylcysteine', 'Ivacaftor', 'Tetracaine', 'Lumacaftor', 'Tezacaftor', 'Abrocitinib', 'Elexacaftor']

# community 7
# drug_list = ['Troglitazone', 'Acetaminophen', 'Minoxidil', 'Rosiglitazone', 'Diethylcarbamazine', 'Sulfasalazine', 'Pseudoephedrine', 'Diflunisal', 'Salicylic acid', 'Bromfenac', 'Balsalazide', 'Papaverine', 'Salsalate', 'Antipyrine', 'Metamizole', 'Nepafenac', 'Triflusal', 'Phenyl salicylate', 'Troglitazone', 'Acetaminophen', 'Minoxidil', 'Rosiglitazone', 'Diethylcarbamazine', 'Sulfasalazine', 'Pseudoephedrine', 'Diflunisal', 'Salicylic acid', 'Bromfenac', 'Balsalazide', 'Papaverine', 'Salsalate', 'Antipyrine', 'Metamizole', 'Nepafenac', 'Triflusal', 'Phenyl salicylate']

# community 8
# drug_list = ['Vitamin A', 'Tramadol', 'Sulpiride', 'Valdecoxib', 'Tretinoin', 'Potassium chloride', 'Ribavirin', 'Mycophenolic acid', 'Phenacemide', 'Nitrazepam', 'Urea', 'Permethrin', 'Sulthiame', 'Hyaluronic acid', 'Xanthinol', 'Sodium sulfate', 'Voretigene neparvovec', 'Vitamin A', 'Tramadol', 'Sulpiride', 'Valdecoxib', 'Tretinoin', 'Potassium chloride', 'Ribavirin', 'Mycophenolic acid', 'Phenacemide', 'Nitrazepam', 'Urea', 'Permethrin', 'Sulthiame', 'Hyaluronic acid', 'Xanthinol', 'Sodium sulfate', 'Voretigene neparvovec']

# community 9
# drug_list = ['Norepinephrine', 'Brimonidine', 'Epinephrine', 'Tolazoline', 'Fenoldopam', 'Oxymetazoline', 'Apraclonidine', 'Guanfacine', 'Yohimbine', 'Celiprolol', 'Droxidopa', 'Xylometazoline', 'Norepinephrine', 'Brimonidine', 'Epinephrine', 'Tolazoline', 'Fenoldopam', 'Oxymetazoline', 'Apraclonidine', 'Guanfacine', 'Yohimbine', 'Celiprolol', 'Droxidopa', 'Xylometazoline']

# community 10
# drug_list = ['Amitriptyline', 'Rufinamide', 'Cenegermin', 'Amitriptyline', 'Rufinamide', 'Cenegermin']

# community 11
# drug_list = ['Abciximab', 'Eptifibatide', 'Antithymocyte immunoglobulin (rabbit)', 'Dextrothyroxine', 'Cisatracurium', 'Tirofiban', 'Triclosan', 'Resorcinol', 'Ferric maltol', 'Eptifibatide', 'Abciximab', 'Antithymocyte immunoglobulin (rabbit)', 'Dextrothyroxine', 'Cisatracurium', 'Tirofiban', 'Triclosan', 'Resorcinol', 'Ferric maltol']

# community 12
drug_list = ['Metformin', 'Dutasteride', 'Tetracosactide', 'Corticotropin', 'Abiraterone', 'Tyloxapol', 'Hexylresorcinol', 'Bremelanotide', 'Glycyrrhizic acid', 'Metformin', 'Dutasteride', 'Tetracosactide', 'Corticotropin', 'Abiraterone', 'Tyloxapol', 'Hexylresorcinol', 'Bremelanotide', 'Glycyrrhizic acid']

# nervous system - N
# atc_class = "nervous system"
# atc_synonims = ["Psychoanaleptics", "Psycholeptics", "Anti-Parkinson drugs",
#                 "Antiepileptics", "Analgesics", "Anesthetics"]

# blood and blood forming organs - B
# atc_class = "blood and blood forming organs"
# atc_synonims = ["Blood substitutes and perfusion solutions", "Antianemic preparations", "Antihemorrhagics", "Antithrombotic agents"]

# cardiovascular system - C
# atc_class = "cardiovascular system"
# atc_synonims = ["Lipid-modifying agents", "Agents acting on the renin-angiotensin system", "Calcium channel blockers", "Beta-blocking agents", "Vasoprotectives", "Peripheral vasodilators", "Diuretics", "Antihypertensives", "Cardiac therapy"]

# antineoplastic and immunomodulating agents - L
# atc_class = "antineoplastic and immunomodulating agents"
# atc_synonims = ["Immunosuppressants", "Immunostimulants", "Endocrine therapy", "Antineoplastic agents"]

# dermatologicals - D
atc_class = "dermatologicals"
atc_synonims = ["Other dermatological preparations", "Anti-acne preparations", "Medicated dressings", "Antiseptics and disinfectants", "Corticosteroids", "dermatological preparations", "Antibiotics and chemotherapeutics for dermatological use", "Antipsoriatics", "Antipruritics", "including antihistamines", "anesthetics", "etc.", "Preparations for treatment of wounds and ulcers", "Emollients and protectives", "Antifungals for dermatological use"]

# musculo-skeletal system - M
# atc_class = "musculo-skeletal system"
# atc_synonims = ["Other drugs for disorders of the musculo-skeletal system", "Drugs for treatment of bone diseases", "Antigout preparations", "Muscle relaxants", "Topical products for joint and muscular pain", "Anti-inflammatory and antirheumatic products"]

# genito urinary system and sex hormones - G
# atc_class = "genito urinary system and sex hormones"
# atc_synonims = ["Urologicals", "Sex hormones and modulators of the genital system", "Other gynecologicals", "Gynecological anti-infectives and antiseptics"]

# systemic hormonal preparations, excluding sex hormones and insulins - H
# atc_class = "systemic hormonal preparations, excluding sex hormones and insulins"
# atc_synonims = ["Calcium homeostasis", "Pancreatic hormones", "Thyroid therapy", "Corticosteroids for systemic use", "Pituitary and hypothalamic hormones and analogues"]

# 1) Combine the main atc_class with atc_synonims
all_synonyms = [atc_class] + atc_synonims

synonyms_or_block = " OR ".join(f'"{syn}"[All Fields]' for syn in all_synonyms)

# -------------------------------------------------------------------------
# 2. Configure Entrez parameters
# -------------------------------------------------------------------------
Entrez.email = "vlad.groza@cs.upt.ro"

# -------------------------------------------------------------------------
# 3. Open a CSV file in write mode
#    We'll store all results in one CSV with an extra column for 'Drug'
# -------------------------------------------------------------------------
csv_filename = "pubmed_results_for_drugs_12.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["Drug", "PMID", "Title", "Authors", "Journal", "PublicationDate", "Abstract"])

    # ---------------------------------------------------------------------
    # 4. Loop over each drug, run the PubMed query, fetch, and parse
    # ---------------------------------------------------------------------
    for drug in drug_list:
        # Construct the search term (example: "Botulinum toxin type B AND nervous system")
        # or you can use more sophisticated queries (e.g., [Title/Abstract], etc.)
        search_term = f'("{drug}"[All Fields]) AND ({synonyms_or_block})'

        # Step A: eSearch to get PMIDs
        search_handle = Entrez.esearch(db="pubmed", term=search_term, retmax=10)
        search_results = Entrez.read(search_handle)
        search_handle.close()

        pmid_list = search_results.get("IdList", [])
        if not pmid_list:
            print(f"No results found for '{drug}'.")
            continue

        # Step B: eFetch to retrieve article data
        fetch_handle = Entrez.efetch(db="pubmed",
                                     id=",".join(pmid_list),
                                     rettype="medline",
                                     retmode="text")
        records = Medline.parse(fetch_handle)
        records = list(records)  # Convert the Medline parse object to a list
        fetch_handle.close()

        print(f"Found {len(records)} articles for '{drug}' - writing to CSV...")

        # Step C: Extract fields from each record and write to CSV
        for article in records:
            pmid = article.get("PMID", "")
            title = article.get("TI", "").replace("\n", " ")
            authors = "; ".join(article.get("AU", []))
            journal = article.get("JT", "")
            pub_date = article.get("DP", "")
            abstract = article.get("AB", "").replace("\n", " ")

            writer.writerow([drug, pmid, title, authors, journal, pub_date, abstract])

        writer.writerow([])
print(f"\nAll done! Results have been saved to '{csv_filename}'.")
