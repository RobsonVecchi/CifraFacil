import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',  // HTML externo
  styleUrls: ['./app.component.css'],   // CSS externo
})
export class AppComponent {
  resultado = '';

  enviarCifra(event: Event) {
    event.preventDefault();
    const form = event.target as HTMLFormElement;

    const data = {
      nome: (form.elements.namedItem('nome') as HTMLInputElement).value,
      banda: (form.elements.namedItem('banda') as HTMLInputElement).value,
      nivel: (form.elements.namedItem('nivel') as HTMLInputElement).value,
      pestana: (form.elements.namedItem('pestana') as HTMLInputElement).checked,
      capotraste: (form.elements.namedItem('capotraste') as HTMLInputElement).checked,
      tonalidade: (form.elements.namedItem('tonalidade') as HTMLInputElement).value,
      genero: (form.elements.namedItem('genero') as HTMLInputElement).value,
      dedilhado: (form.elements.namedItem('dedilhado') as HTMLInputElement).checked,
      levada: (form.elements.namedItem('levada') as HTMLInputElement).checked,
    };

    fetch('http://localhost:8000/cifras/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then((res) => {
        if (!res.ok) throw new Error('Erro na requisição');
        return res.json();
      })
      .then(() => {
        this.resultado = 'Cifra enviada com sucesso!';
        form.reset();
      })
      .catch((err) => {
        this.resultado = 'Erro: ' + err.message;
      });
  }
}