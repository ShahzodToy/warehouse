from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductMaterial, Warehouse


class ProductMaterialRequestView(APIView):
    def post(self, request):
        product_code = self.request.data['product_code']
        quantity = self.request.data['quantity']

        product = Product.objects.filter(code=product_code).first()
        product_material = ProductMaterial.objects.filter(product=product)

        if not product:
            return Response({'message':"Product not found with this code"})
        results = {
            'product_name':product.name,
            'product_qty':quantity,
            'product_materials':[]
        }
        for pm in product_material:
            required_qty = pm.quantity * quantity
            warehouses = Warehouse.objects.filter(material=pm.material)
            for warehouse in warehouses:
                if required_qty <= warehouse.remainder:
                   results["product_materials"].append({
                        "warehouse_id": warehouse.id,
                        "material_name": pm.material.name,
                        "qty": required_qty,
                        "price": warehouse.price
                    })
                   required_qty = 0
                else:
                    results["product_materials"].append({
                        "warehouse_id": warehouse.id,
                        "material_name": pm.material.name,
                        "qty": warehouse.remainder,
                        "price": warehouse.price
                    })
                    required_qty -= warehouse.remainder
            if required_qty > 0:
                results["product_materials"].append({
                    "warehouse_id": None,
                    "material_name": pm.material.name,
                    "qty": required_qty,
                    "price": None
                })


        return Response({"result": results})