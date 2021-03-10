import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { AlbumComponent } from './album/album.component';
import { AlbumDetailComponent } from './album-detail/album-detail.component';
import { AlbumPhotoComponent } from './album-photo/album-photo.component';
import {AlbumServiceService} from './album-service.service';



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    AlbumComponent,
    AlbumDetailComponent,
    AlbumPhotoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [AlbumServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
