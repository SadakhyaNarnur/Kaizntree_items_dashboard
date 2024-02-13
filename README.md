# Kaizntree Inventory Management Service
### Api documentation
#### Listing the items in the dashboard
- 
    **GET** 
    http://127.0.0.1:8000/items/

    **Output:**
  ```json
  [
      {
          "SKU": "BWAX",
          "Name": "BeesWax",
          "Tags": "Etsy,Bing",
          "category": 1,
          "In_stock": "200.00",
          "Available_stock": "50.00"
      }
  ]
#### Adding a new item
**POST**
http://127.0.0.1:8000/items/
Body: {
        "SKU": "BWAX",
        "Name": "BeesWax",
        "Tags": "Etsy,Bing",
        "category": 1,
        "In_stock": "200.00",
        "Available_stock": "50.00"
    }

Output: Added Successfully

Editing the item 
PUT
http://127.0.0.1:8000/items/1
Body: {
        "SKU": "BWAX",
        "Name": "BeesWax",
        "Tags": "Etsy",
        "category": 1,
        "In_stock": "200.00",
        "Available_stock": "50.00"
    }

Output: Updated Successfully
Deleting the item
DELETE
http://127.0.0.1:8000/items/1
Output: Deleted Successfully
Listing the categories
GET
http://127.0.0.1:8000/category/

[
    {
        "id": 1,
        "category_name": "Raw Materials"
    },
    {
        "id": 2,
        "category_name": "Bundles"
    },
    {
        "id": 3,
        "category_name": "Finished Products"
    }
]
Adding a new category
POST
http://127.0.0.1:8000/category/
Body: {
        "category_name": "Appliances"
    }

Output: Added Successfully

Editing the item 
PUT
http://127.0.0.1:8000/items/4
Body: {
        "category_name": "Appliance"
    }

Output: Updated Successfully
Deleting the item
DELETE
http://127.0.0.1:8000/items/4

Output: Deleted Successfully

Count of items and categories
PUT
http://127.0.0.1:8000/counts/

Output:
{
    "items_count": 1,
    "categories_count": 4
}

Sorting the items based on field names
GET
http://127.0.0.1:8000/items/?sort_by=Name

Output:
[
    {
        "SKU": "BWAX",
        "Name": "BeesWax",
        "Tags": "Etsy,Bing",
        "category": 1,
        "In_stock": "200.00",
        "Available_stock": "50.00"
    },
    {
        "SKU": "BSWX",
        "Name": "Beeswax",
        "Tags": "Etsy, Bing",
        "category": 2,
        "In_stock": "60.00",
        "Available_stock": "188.00"
    },
    {
        "SKU": "CLRP",
        "Name": "Colorful Pens",
        "Tags": "Etsy",
        "category": 2,
        "In_stock": "150.00",
        "Available_stock": "15.00"
    },
    {
        "SKU": "HTR",
        "Name": "Heater",
        "Tags": "Bing",
        "category": 3,
        "In_stock": "0.00",
        "Available_stock": "0.00"
    }
]

Searching for a word 
GET
http://127.0.0.1:8000/items/?search=pen
 Output:
[
    {
        "SKU": "CLRP",
        "Name": "Colorful Pens",
        "Tags": "Etsy",
        "category": 2,
        "In_stock": "150.00",
        "Available_stock": "15.00"
    }
]


### Deployment
'Using the docker file provided to create your own docker image and run on any platform that supports docker.
'

### Start Application
'Application flow starts at http://localhost:8000/login/'