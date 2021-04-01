import { Component } from '@angular/core';
import {preserveWhitespacesDefault} from '@angular/compiler';

export interface Todo {
  id: number;
  status: boolean;
  type: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  apptitle = 'Just';

  public todos: Todo[] = [
    {id: 1, status: false, type: 'купи хлеб'},
    {id: 2, status: true, type: 'купи энергетик'},
    {id: 3, status: true, type: 'купи мозг'},
  ];

  onToggle(id: number) {
    const inx = this.todos.findIndex(predicate: t => t.d === id);
    this.todos[id].status = !this.todos[id].status;
  }
}
