import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import {Todo} from '../app.component';

@Component({
  selector: 'app-to-do',
  templateUrl: './to-do.component.html',
  styleUrls: ['./to-do.component.css']
})
export class ToDoComponent implements OnInit {
  @Input() todos: Todo[] = [];
  @Output() onToggle = new EventEmitter<number>();
  constructor() { }
  ngOnInit(): void {
  }

  // onChange(id: number) {
  //   this.onToggle.emit(id);
  // }

}
