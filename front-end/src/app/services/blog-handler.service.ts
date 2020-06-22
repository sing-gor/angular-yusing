import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, pipe, BehaviorSubject } from 'rxjs';

import { Router } from '@angular/router';
import { ServicesModule } from './services.module';
import { BlogList, BlogDetail, BlogBadges } from '../models/blog.type';
import { map, zip, mapTo } from 'rxjs/internal/operators';
@Injectable({
  providedIn: ServicesModule,
})
export class BlogHandlerService {
  // config
  public tagsData = new BehaviorSubject<BlogBadges[]>([
    {
      title: '',
      body: '',
      slug: '',
    },
  ]);
  public categoriesData = new BehaviorSubject<BlogBadges[]>([
    {
      title: '',
      body: '',
      slug: '',
    },
  ]);
  baseUrl = 'http://127.0.0.1:8000/api/';
  baseTag = '?/format=json';
  public httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  constructor(private http: HttpClient, private router: Router) {}
  getBlogDetail(slug: string): Observable<BlogDetail> {
    return this.http
      .get(this.baseUrl + 'blog/' + slug + this.baseTag)
      .pipe(map((res: BlogDetail) => res));
  }
  getBlogList(parms): Observable<BlogList> {
    return this.http.get<BlogList>(this.baseUrl + 'blog/' + this.baseTag, {
      params: parms,
    });
    // .pipe(map((res: BlogList) => res));
  }

  getCategories(): Observable<BlogBadges[]> {
    return this.http.get<BlogBadges[]>(
      this.baseUrl + 'category/' + this.baseTag
    );
  }

  getTags(): Observable<BlogBadges[]> {
    return this.http.get<BlogBadges[]>(this.baseUrl + 'tags/' + this.baseTag);
  }

  changeTagsMessage(message: BlogBadges[]): void {
    this.tagsData.next(message);
  }
  changeCategoriesMessage(message: BlogBadges[]): void {
    this.categoriesData.next(message);
  }
}
