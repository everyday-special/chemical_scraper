# chemical_scraper
## Scraping Chemicals from Recent Nature Publications

I was interested in creating a program that scrapes data from scientific literature and analyzes the article text. Working in an HIV focused laboratory, I decided I would look into that area of literature. As a lot of our research is focused on finding potential cures, I thought it would be interesting to look at the drugs being mentioned in the literature. Any drug mentioned in the literature might be being looked for its therapeutic potential. It might also be interesting to see what drugs show up that we are looking at in our lab.

## Chemical Reference List

First I needed a comprehensive list of chemicals/drugs to use as a reference. I decided to use the [ChEMBLdb](https://www.ebi.ac.uk/chembl/) since you can download their database into SQL. ChEMBLdb has a wealth of information, but for my purposes I only needed two things: drug names (trade, common, etc.) and ChEMBL IDs (the chemicals ID in the ChEMBL database). These were extracted from the database in two csv files. One csv file contained drug names ('synonyms') and internal identifier numbers ('molreg no') and the other file contained ChEMBL IDs and the internal identifier numbers ('molreg no'). These files were named 'synonyms.csv' and 'chemblids.csv', respectively. I created a [script]() that links the synonyms with the ChEMBL IDs using the molreg numbers, putting the linked synonyms and ChEMBL IDs in a csv file called 'synonyms_chemblids.csv'.

## Scraping Article Data from Recent Nature Publications

After setting up my chemical reference file, I needed to get some article data to investigate. I started off by searching 'HIV' in Nature, which gives me the 50 most HIV-relevent articles. I then made a [script]() analyzing this search result. Using the Beautiful Soup Library made it easy to pull data from each of these 50 articles including the article title, article URL, article type, publication date, whether the article is open or not, and the article text (if the article is open). This data was stored in a csv file called 'article_scrapings.csv'.

## Finding the Chemicals Mentioned in the Articles

I then created a final script that cross references the chemicals and the article text. For each chemical that was mentioned in an article some data was saved. This included the amount of articles the chemical was mentioned in, the synonyms it was mentioned by, the titles of the articles it was mentioned in, and the url of the chemical in the online ChEMBL database. This information was then saved in a csv file called 'chemical_scraping_hiv.csv'. You can find the first 5 entries of 'chemical_scrapings_hiv.csv' below.

| chembl id  |  Number of Articles Mentioned |  Names Used | Mentioned in Articles  | chembl url  |
|---|---|---|---|---|
| CHEMBL6  | 1  | ['indomethacin']  |  ['Mesenchymal stem cells are attracted to latent HIV-1-infected cells and enable virus reactivation via a non-canonical PI3K-NFκB signaling pathway'] | https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL6  |
| CHEMBL1202  | 5  |  ['cipro'] | ['Cellular TRIM33 restrains HIV-1 infection by targeting viral integrase for proteasomal degradation', 'Single Cell Profiling Reveals PTEN Overexpression in Influenza-Specific B cells in Aging HIV-infected individuals on Anti-retroviral Therapy', 'Comparison of visceral fat measurement by dual-energy X-ray absorptiometry to computed tomography in HIV and non-HIV', 'A Naturally Occurring Polymorphism in the HIV-1 Tat Basic Domain Inhibits Uptake by Bystander Cells and Leads to Reduced Neuroinflammation', 'Mesenchymal stem cells are attracted to latent HIV-1-infected cells and enable virus reactivation via a non-canonical PI3K-NFκB signaling pathway']  |  https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL1202 |
| CHEMBL405  |  2 |  ['amphetamine'] |  ['Methamphetamine functions as a novel CD4+ T-cell activator via the sigma-1 receptor to enhance HIV-1 infection', 'HIV-infected macrophages and microglia that survive acute infection become viral reservoirs by a mechanism involving Bim'] |  https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL405 |
|  CHEMBL263881 | 1  | ['lsd']  | ['Single Cell Profiling Reveals PTEN Overexpression in Influenza-Specific B cells in Aging HIV-infected individuals on Anti-retroviral Therapy']  | https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL263881  |
|  CHEMBL413 |  2 |  ['rapamycin'] | ['Integrated systems approach defines the antiviral pathways conferring protection by the RV144 HIV vaccine', 'Mesenchymal stem cells are attracted to latent HIV-1-infected cells and enable virus reactivation via a non-canonical PI3K-NFκB signaling pathway']  |  https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL413 |
