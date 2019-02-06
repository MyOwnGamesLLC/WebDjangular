import { RouterModule, Routes } from "@angular/router";
import { NgModule } from "@angular/core";
import { ShippingMethodModel } from "../data/models/ShippingMethod.model";
import { CatalogRuleModel } from "../data/models/CatalogRule.model";
import { CartRuleModel } from "../data/models/CartRule.model";
import { OrderModel } from "../data/models/Order.model";
import { CategoryModel } from "../data/models/Category.model";
import { ProductTypeModel } from "../data/models/ProductType.model";
import { ProductModel } from "../data/models/Product.model";
import { ProductAttributeModel } from "../data/models/ProductAttribute.model";
import { ScaffoldModule } from "@core/builder/src/lib/scaffold/scaffold.module";
import { CartTermModel } from "../data/models/CartTerm.model";

const routes: Routes = [
  {
    path: 'store',
    children: [
      {
        path: 'catalog',
        children: [
           {
            path: 'products',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: ProductModel,
              title: 'Products',
              path: 'store/catalog/products'
            }
          },
          {
            path: 'categories',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: CategoryModel,
              title: 'Categories',
              path: 'store/catalog/categories'
            }
          },
          {
            path: 'types',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: ProductTypeModel,
              title: 'Product Type',
              path: 'store/catalog/types'
            }
          },
          {
            path: 'attributes',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: ProductAttributeModel,
              title: 'Product Attribute',
              path: 'store/catalog/attributes'
            }
          },
        ]
      },
      {
        path: 'orders',
        loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
        data: {
          model: OrderModel,
          title: 'Orders',
          path: 'store/orders'
        }
      },
      {
        path: 'rules',
        children: [
          {
            path: 'cart-rules',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: CartRuleModel,
              title: 'Cart Rules',
              path: 'store/rules/cart-rules'
            }
          },
          {
            path: 'catalog-rules',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: CatalogRuleModel,
              title: 'Catalog Rules',
              path: 'store/rules/catalog-rules'
            },
          },
          {
            path: 'cart-terms',
            loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
            data: {
              model: CartTermModel,
              title: 'Cart Terms',
              path: 'store/rules/cart-terms'
            },
          },
        ],
      },
      {
        path: 'shipping-methods',
        loadChildren: '@core/builder/src/lib/scaffold/scaffold.module#ScaffoldModule',
        data: {
          model: ShippingMethodModel,
          title: 'Shipping methods',
          path: 'store/shipping-methods'
        }
      },
    ]
  },

]

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class StoreAdminRoutingModule {
}
