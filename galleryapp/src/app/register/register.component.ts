import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';
import { RegisterService } from '../services/register/register.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  public registerForm: FormGroup;

  constructor(private route: ActivatedRoute,
    private registerService: RegisterService,
    private location: Location
  ) { }


  ngOnInit() {
    this.registerForm = new FormGroup({
      username: new FormControl(),
      first_name: new FormControl(),
      last_name: new FormControl(),
      password: new FormControl(),
      email: new FormControl(),
      pais: new FormControl(),
      ciudad: new FormControl(),
      foto: new FormControl(),
    });
  }

  register() {
    var result = 
      this.registerService.register(
      this.registerForm.get('username').value,
      this.registerForm.get('password').value,
      this.registerForm.get('first_name').value,
      this.registerForm.get('last_name').value,
      this.registerForm.get('email').value,
      this.registerForm.get('pais').value,
      this.registerForm.get('ciudad').value,
      this.registerForm.get('foto').value);
  } 

}
