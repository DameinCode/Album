import { Component, OnInit } from '@angular/core';
import {Album, Photo, AlbumServiceService} from '../album-service.service';
import {RouterModule} from "@angular/router";
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-photo',
  templateUrl: './album-photo.component.html',
  styleUrls: ['./album-photo.component.css']
})
export class AlbumPhotoComponent implements OnInit {
  album: Album = {id:0,userId:0,title:''};
  photos: Photo[] = [];
  constructor(private route: ActivatedRoute,
              public albumServiceService: AlbumServiceService,
              private location: Location) { }

  ngOnInit(): void {
    // @ts-ignore
    this.getPhotos();
  }
  getPhotos(){
    // @ts-ignore
    const id = +this.route.snapshot.paramMap.get('id');

    this.albumServiceService.gogoP(id)
      .subscribe(photos => this.photos = photos);
  }
  goBack(): void {
    this.location.back();
  }
}
