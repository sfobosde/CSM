import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LeftMenuComponent } from './LeftMenu/lefmenu.component'

@NgModule({
  declarations: [
    AppComponent,
    LeftMenuComponent
  ],
  imports: [
    BrowserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
