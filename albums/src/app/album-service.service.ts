import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import {tap} from 'rxjs/operators';
import { Observable } from 'rxjs';
// next() — принимает значение, которое будет возвращено функции-обработчику;
// Все операторы преобразования данных объявляются в методе pipe() через запятую

export interface Album {
  userId: number;
  id: number;
  title: string;
}

export interface Photo {
  "albumId": number,
  "id": number,
  "title": string,
  "url": string,
  "thumbnailUrl": string
}

@Injectable({
  providedIn: 'root'
})
export class AlbumServiceService {
  albums: Album[] = [];
  photos: Photo[] = [];
  index = 100;

  constructor(public require: HttpClient) { }
  gogoA(): Observable<Album[]>{
    return this.require.get<Album[]>('https://jsonplaceholder.typicode.com/albums').pipe(tap( albums => this.albums = albums));
  }

  gogoP(id:number): Observable<Photo[]>{
    return this.require.get<Photo[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`).pipe(tap( photos => this.photos = photos));
  }

  removeIt(alb: Album): void{
    this.albums.slice(this.albums.indexOf(alb), 1);
    this.index --;
  }

  addIt(title: string, userId: number): void {
    this.albums.push({userId: userId, id: this.index+1, title: title});
    this.index ++;
  }
}
