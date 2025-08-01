import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
    <h1>Enviar Cifra</h1>
    <form (submit)="enviarCifra($event)">
      <label>
        Nome:
        <input type="text" name="nome" placeholder="Nome" required />
      </label>
      <br />
      <label>
        Banda:
        <input type="text" name="banda" placeholder="Banda" required />
      </label>
      <br />
      <label>
        Nível:
        <input type="text" name="nivel" placeholder="Nivel" required />
      </label>
      <br />
      <label>
        Pestana:
        <input type="checkbox" name="pestana" />
      </label>
      <br />
      <label>
        Capotraste:
        <input type="checkbox" name="capotraste" />
      </label>
      <br />
      <label>
        Tonalidade:
        <input type="text" name="tonalidade" placeholder="Tonalidade" />
      </label>
      <br />
      <label>
        Gênero:
        <input type="text" name="genero" placeholder="Genero" />
      </label>
      <br />
      <label>
        Dedilhado:
        <input type="checkbox" name="dedilhado" />
      </label>
      <br />
      <label>
        Levada:
        <input type="checkbox" name="levada" />
      </label>
      <br />
      <button type="submit">Enviar</button>
    </form>

    <p *ngIf="resultado">{{ resultado }}</p>
  `,
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

