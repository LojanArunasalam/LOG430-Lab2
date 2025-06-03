from sqlalchemy.orm import sessionmaker

import controller
from controller import session 

def main():
    message = """
======= CAISSE =======
1 - Rechercher un produit
2 - Enregistrer une vente
3 - Consulter le stock d'un produit
4 - Exit
--------------"""

    while True:
        print(message)
        choice = int(input("Choisissez une option: "))

        if choice == 1:
            id = int(input("Mettez l'ID du produit: "))
            product = controller.get_product_by_id(id) 

            if product:
                print(f"Name: {product.name}, Description: {product.description}")
            else:
                print("Produit non trouvé")
        elif choice == 2:
            lignes_ventes = []
            while True: 
                product_id = int(input("Mettez l'id du produit que vous voulez acheter [0 pour quitter]: "))
                
                if product_id == 0:
                    break
                
                product = controller.get_product_by_id(product_id)

                if not product:
                    print("Produit pas trouvé")
                    continue

                quantite_voulu = int(input("Combien: "))
                if product.stock - quantite_voulu < 0:
                    print("Pas assez en stock")
                    continue
                    
                controller.update_stock(product, quantite_voulu)
                session.add(product)
                session.commit()
                ligne_vente = controller.create_line_sale(product, quantite_voulu)
                lignes_ventes.append(ligne_vente)
                        

            sale = controller.create_sale(lignes_ventes)
            session.add(sale)
            session.commit()
        elif choice == 3:
            id = int(input("Mettez l'ID du produit: "))
            stocks =  controller.get_stock(id)

            for i, stock in enumerate(stocks):
                print(f"Magasin {i+1}: {stock}")
        elif choice == 4:
            break
        else:
            print("Mauvaise input")
            continue

if __name__ == "__main__":
    main()
