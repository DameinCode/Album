import { Component, OnInit } from '@angular/core';
import { Album } from '../album-service.service';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { AlbumServiceService } from '../album-service.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {

  album: Album | undefined = {id: 1, userId: 0, title: ''};
  // idd: string;
  // id = null;
  constructor(
    public routing: ActivatedRoute,
    public albumServiceService: AlbumServiceService,
    public location: Location
  ) {
  }

  ngOnInit(): void {
    const idd = +this.routing.snapshot.params['idd'];
    if (this.albumServiceService.albums.find(album => album.id === idd)) {
      this.album = this.albumServiceService.albums.find(album => album.id === idd);
    }
  }

  goBack(): void {
    this.location.back();
  }

}
