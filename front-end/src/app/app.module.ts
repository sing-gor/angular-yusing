import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { CoreModule } from './core/core.module';
import { SafeHtmlPipe } from './safe-html.pipe';

@NgModule({
  declarations: [AppComponent],
  imports: [CoreModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
