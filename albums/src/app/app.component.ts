import { Component, OnInit } from '@angular/core';
import { AlbumServiceService } from './album-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(public albumServiceService: AlbumServiceService) {
    // this.albumServiceService.gogoA().pipe().subscribe();
  }
  ngOnInit():void {
    this.albumServiceService.gogoA().pipe().subscribe();
  }

}

