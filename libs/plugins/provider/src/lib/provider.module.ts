import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PluginProviderComponent } from "./provider.component";
import { PluginProviderCheckoutModule } from "./components/checkout/checkout.module";

import { PluginProviderPlansComponent } from "./components/plans/plans.component";
import { PluginProviderPricingInternetHorizontalComponent } from "./components/plans/pricing/internet-horizontal/internet-horizontal.component";
import { PluginPricingComboVerticalComponent } from "./components/plans/pricing/combo-vertical/combo-vertical.component";
import { PluginProviderPricingInternetVerticalComponent } from "./components/plans/pricing/internet-vertical/internet-vertical.component";
import { PluginProviderPricingTelephoneVerticalComponent } from "./components/plans/pricing/telephone-vertical/telephone-vertical.component";
import { PluginProviderPricingTvVerticalComponent } from "./components/plans/pricing/tv-vertical/tv-vertical.component";
import { PluginProviderError404Component } from './components/errors/404/404.component';
import { PluginProviderError500Component } from './components/errors/500/500.component';
import { ProviderCheckoutService } from "./data/services/provider-checkout.service";
import { PluginProviderCityListComponent } from './components/city-list/city-list.component';
import { PluginProviderCityCoverageComponent } from './components/city-coverage/city-coverage.component';
import { AgmCoreModule } from '@agm/core';
import { RouterModule } from '@angular/router';
import {CartService} from "@plugins/store/src/lib/data/services/cart.service";
import { PluginProviderDialogComponent } from './components/dialog.component';



const MODULES = [
  CommonModule,
  PluginProviderCheckoutModule,

];

const COMPONENTS = [
  PluginProviderComponent,
  PluginProviderCityListComponent,
  PluginProviderPlansComponent,
  PluginProviderCityCoverageComponent,
  PluginProviderPricingInternetHorizontalComponent,
  PluginPricingComboVerticalComponent,
  PluginProviderPricingInternetVerticalComponent,
  PluginProviderPricingTelephoneVerticalComponent,
  PluginProviderPricingTvVerticalComponent,
  PluginProviderError404Component,
  PluginProviderError500Component,
  PluginProviderDialogComponent
];

const SERVICES = [
  CartService,
  ProviderCheckoutService,

];

@NgModule({
  imports: [
    ...MODULES,
    AgmCoreModule,
    RouterModule
  ],
  exports: [
    ...COMPONENTS,
    ...MODULES

  ],
  entryComponents: [...COMPONENTS],
  declarations: [...COMPONENTS],
  providers: [...SERVICES]
})
export class PluginProviderModule {
}
