import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LeftMenuComponent } from './LeftMenu/leftmenu.component'
import { MainMenuComponent} from './Main/main.component'

@NgModule({
  declarations: [
    AppComponent,
    LeftMenuComponent,
    MainMenuComponent
  ],
  imports: [
    BrowserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
