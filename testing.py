import requests
import uuid
import random
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/csm"

def post(entity, action, data):
    url = f"{BASE_URL}/{entity}/{action}"
    print(f"POST {url}")
    response = requests.post(url, json=data)
    if not response.ok:
        print(f"ERROR: {response.status_code} - {response.text}")
    return response.json()

def main():
    # 1. Create a material
    material_data = {
        "name": "Test Material"
    }
    material = post("material", "add", material_data)

    print(material)

    # 2. Create a sheet for the material
    sheet_data = {
        "lenght": 1000,
        "width": 2000,
        "fitness": 16,
        "material_id": material["id"]
    }
    post("sheet", "add", sheet_data)

    # 3. Create a template
    template_data = {
        "file_link": "http://example.com/template.dxf",
        "name": "Test Template",
        "length": 500,
        "width": 300,
        "fitness": 16,
        "additional_data": "Test info"
    }
    template = post("template", "add", template_data)

    # 4. Create a detail based on template and material
    detail_data = {
        "template_id": template["id"],
        "material_id": material["id"],
        "name": "Test Detail",
        "addtitional_data": "Additional info"
    }
    detail = post("detail", "add", detail_data)

    # 5. Create an order with that detail
    order_data = {
        "name": "Test Order",
        "orderDate": datetime.now().strftime('%Y-%m-%d'),
        "details": [
            {
                "detail_id": detail["id"],
                "count": 5
            }
        ]
    }
    order = post("order", "add", order_data)

    # 6. Call generate_maps
    print("Generating cutting maps...")
    response = requests.post(f"{BASE_URL}/order/create_maps")
    if not response.ok:
        print(f"ERROR on map generation: {response.status_code} - {response.text}")
    else:
        print("Cutting maps generated successfully.")

if __name__ == "__main__":
    main()
