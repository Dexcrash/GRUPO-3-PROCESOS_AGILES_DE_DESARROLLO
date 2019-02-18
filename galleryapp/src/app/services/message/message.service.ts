import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MessageService {

  messages: string[] = [];
  
  auth: Boolean = false;

  id: number;

  add(message: string) {
    this.messages.push(message);
  }
  clear() {
    this.messages = [];
  }

  authenticate(bol: Boolean) {
    this.auth = bol; 
  }

  userId(id: number) {
    this.id = id; 
  }
}
