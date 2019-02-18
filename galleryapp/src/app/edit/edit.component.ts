import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';
import { EditService } from '../services/edit/edit.service';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit {

  public editForm: FormGroup;

  constructor(private route: ActivatedRoute,
    private editService: EditService,
    private location: Location
  ) { }


  ngOnInit() {
    this.editForm = new FormGroup({
      first_name: new FormControl(),
      last_name: new FormControl(),
      email: new FormControl(),
      pais: new FormControl(),
      ciudad: new FormControl(),
      foto: new FormControl(),
    });
  }

  edit() {
    var result = 
      this.editService.edit(
      this.editForm.get('first_name').value,
      this.editForm.get('last_name').value,
      this.editForm.get('email').value,
      this.editForm.get('pais').value,
      this.editForm.get('ciudad').value,
      this.editForm.get('foto').value);
  } 
}
