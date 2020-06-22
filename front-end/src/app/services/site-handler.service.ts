import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, pipe, BehaviorSubject } from 'rxjs';

import { Router } from '@angular/router';
import { ServicesModule } from './services.module';
import { map, zip, mapTo } from 'rxjs/internal/operators';
import { SiteData } from '../models/site.type';

@Injectable({
  providedIn: ServicesModule,
})
export class SiteHandlerService {
  baseUrl = 'http://127.0.0.1:8000/api/';
  baseTag = '?/format=json';
  public httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };
  constructor(private http: HttpClient, private router: Router) {}
  getSiteData(): Observable<SiteData> {
    return this.http
      .get(this.baseUrl + 'sitedata/' + 1 + this.baseTag)
      .pipe(map((res: SiteData) => res));
  }
}
