## Project Overview: Wine Ratings Data Preparation

### Data-Processing Steps

1. **Data Loading:**  
   Imported the dataset, focusing on the following key columns:
   - `country`
   - `description`
   - `points`
   - `price`
   - `province`
   - `variety`
   - `winery`

2. **Data Cleaning:**  
   - **Removed Missing Values:**  
     Dropped rows with missing data in any of the selected columns.

3. **Handled Duplicates:**  
   - **Exact Matches:**  
     Excluded exact duplicates with identical descriptions.
   - **Different Descriptions:**  
     Merged ratings and combined descriptions for entries representing the same wine rated by different users.
