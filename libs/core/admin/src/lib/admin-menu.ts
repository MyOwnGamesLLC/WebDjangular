import {NbMenuItem} from '@nebular/theme';
import {ScaffoldModule} from "@webdjangular/core/admin";
import {ProductModel} from "../../../../plugins/store/src/lib/data/models/Product.model";

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/',
  },
  {
    title: 'Medias',
    icon: 'fas fa-file-image',
    link: '/media',
  },
  {
    title: 'Pages',
    icon: 'fas fa-file-alt',
    link: '/pages',
  },
  {
    title: 'Store',
    icon: 'fas fa-shopping-cart',
    children: [
      {
        title: 'Products',
        link: '/store/products'
        //data: {
        //  permission: [
        //    { label: 'store', action: 'list_products' }
        //  ]
      },
      {
        title: 'Orders',
        link: '/store/orders',
      },
      {
        title: 'Discounts',
        children: [
          {
            title: 'Vouchers',
            link: '/store/vouchers',
          },
          {
            title: 'Sales',
            link: '/store/sales',
          },
        ]
      },
      {
        title: 'Shipping methods',
        link: '/store/shipping-methods',
      },
    ]
  },
  {
    title: 'Provider',
    icon: 'fas fa-globe',
    children: [
      {
        title: 'Cities',
        link: '/cities',
        data: {
          permission: [
            {label: 'provider', action: 'list_cities'}
          ]
        }
      }
    ]
  },
  {
    title: 'Forms',
    icon: 'fab fa-wpforms',
    link: '/forms',
  },
  {
    title: 'System',
    icon: 'fas fa-cog',
    children: [
      {
        title: 'Themes',
        link: '/core_themes',
        data: {
          permission: [
            {label: 'webdjango', action: 'list_core_theme'},
          ]
        }
      },
      {
        title: 'Plugins',
        link: '/core_plugins',
        data: {
          permission: [
            {
              label: 'webdjango', // Name of the plugin on WebDjango side
              action: 'list_core_plugin'
            },
          ]
        }
      },
      {
        title: 'Users',
        link: '/user',
        data: {
          permission: [
            {label: 'users', action: 'list_user'},
          ]
        }
      },
      {
        title: 'Groups',
        link: '/group',
        data: {
          permission: [
            {label: 'auth', action: 'list_group'}
          ]
        }
      },

      {
        title: 'Configs',
        data: {
          core_configs: true,
        },
        children:
          [
            {
              title: 'Websites',
              link: '/core_websites',
              data: {
                permission: [
                  {label: 'webdjango', action: 'list_core_website'}
                ]
              }
            }
          ]
      }
    ]
  },
];
