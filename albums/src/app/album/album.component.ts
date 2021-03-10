import { Component } from '@angular/core';
import { AlbumServiceService} from '../album-service.service';
import { Album } from '../album-service.service';

@Component({
  selector: 'app-album',
  templateUrl: './album.component.html',
  styleUrls: ['./album.component.css']
})
export class AlbumComponent {
  toCheck1 = '';
  toCheck2 = '';
  constructor(public albumServiceService: AlbumServiceService) { }

  removeIt(album: Album): void{
    this.albumServiceService.removeIt(album);
  }

  addIt(title: string, userId: string): void {
    this.toCheck1 = title.split(' ').join('');
    this.toCheck2 = userId.split(' ').join('');
    if(this.toCheck2 === '' || this.toCheck1 === '') {
      alert('Input a text!');
    }
    else {
      this.albumServiceService.addIt(title, Number(userId));
    }
  }

}
