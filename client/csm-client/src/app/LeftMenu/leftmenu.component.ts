import { Component } from '@angular/core';

@Component({
  selector: 'leftmenu',
  templateUrl: './leftmenu.component.html',
  styleUrls: [`./leftmenu.component.scss`] 
})
export class LeftMenuComponent {
  title = 'Cutting Sheet Material';

  // Открытые панели.
  public openNav() {
    let mySidepanel = document.getElementById("mySidepanel");
    if (mySidepanel) {
      mySidepanel.style.width = "250px";
    }
  }

  // Закрытие панели
  public closeNav() {
    let mySidepanel = document.getElementById("mySidepanel");

    if (mySidepanel) {
      mySidepanel.style.width = "0";
    }
  }
}
