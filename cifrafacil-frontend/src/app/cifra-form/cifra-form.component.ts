import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cifra-form',
  templateUrl: './cifra-form.component.html',
  styleUrls: ['./cifra-form.component.css']
})
export class CifraFormComponent {
  cifra = {
    nome: '',
    banda: '',
    nivel: '',
    pestana: false,
    capotraste: false,
    tonalidade: '',
    genero: '',
    dedilhado: false,
    levada: false
  };

  resposta: any;

  constructor(private http: HttpClient) {}

  enviarCifra() {
    this.http.post('http://localhost:8000/cifras/', this.cifra)
      .subscribe({
        next: (res) => this.resposta = res,
        error: (err) => console.error(err)
      });
  }
}
