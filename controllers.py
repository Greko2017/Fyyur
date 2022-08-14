from unicodedata import name
from app import app
from flask import Flask,jsonify, render_template, request, Response, flash, redirect, url_for
from models import *
from forms import ArtistForm, VenueForm
import sys
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  error = False
  try:
  # TODO: modify data to be the data object returned from db insertion
    venue = Venue(
        genres=request.form.getlist('genres'),
        name=request.form['name'],
        address=request.form['address'],
        phone=request.form['phone'],
        website_link=request.form['website_link'],
        image_link=request.form['image_link'],
        facebook_link=request.form['facebook_link'],
        seeking_talent=request.form.get('seeking_talent', False),
        seeking_description=request.form['seeking_description']
    )
    area = Area.query.filter_by(state=request.form['state']).filter_by(city=request.form['city']).first()
    if not area:
        area = Area(state=request.form['state'],city=request.form['city'])
    area.venues.append(venue)
    # venue.area = area[0]
    db.session.add(area)
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
    # on successful db insert, flash success
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
    return redirect(url_for('venues') )
  else:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
  return render_template('pages/home.html')


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  data=[{
    "id": 4,
    "name": "Guns N Petals",
  }, {
    "id": 5,
    "name": "Matt Quevedo",
  }, {
    "id": 6,
    "name": "The Wild Sax Band",
  }]
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)


#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  error = False
  try:
    # TODO: modify data to be the data object returned from db insertion
    artist = Artist(
        genres=request.form['genres'],
        name=request.form['name'],
        # address=request.form['address'],
        phone=request.form['phone'],
        website_link=request.form['website_link'],
        image_link=request.form['image_link'],
        facebook_link=request.form['facebook_link'],
        seeking_talent=request.form.get('seeking_venue', False),
        seeking_description=request.form['seeking_description']
    )
    area = Area.query.filter_by(state=request.form['state']).filter_by(city=request.form['city']).first()
    if not area:
        area = Area(state=request.form['state'],city=request.form['city'])
    area.artists.append(artist)
    # artist.area = area[0]
    db.session.add(area)
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if not error:
    # on successful db insert, flash success
    flash('artist ' + request.form['name'] + ' was successfully listed!')
    return redirect( url_for('artists') )
  else:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. artist ' + data.name + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('An error occurred. artist ' + request.form['name'] + ' could not be listed.')
  return render_template('pages/home.html')
  