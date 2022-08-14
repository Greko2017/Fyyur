# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)
from app import db
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# TODO: implement any missing fields, as a database migration using Flask-Migrate


class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String())
    city = db.Column(db.String(), nullable=False)
    venues = db.relationship('Venue', backref='area', lazy=True)
    artists = db.relationship('Artist', backref='area', lazy=True)

    def __repr__(self):
        return f'<Area {self.city} {self.state}>'


# shows_venues_artists = db.Table('shows',
#     db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True),
#     db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
#     db.Column('start_time', db.DateTime, nullable=True)
# )
# Association Object ref : https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#association-object
class Show(db.Model):
    __tablename__ = 'shows'
    venue_id = db.Column(db.ForeignKey("venues.id"), primary_key=True)
    artist_id = db.Column(db.ForeignKey("artists.id"), primary_key=True)
    start_time = db.Column(db.DateTime())
    artist = db.relationship("Artist", back_populates="venues")
    venue = db.relationship("Venue", back_populates="artists")

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # state = db.Column(db.String())
    # city = db.Column(db.String(), nullable=True)
    # num_upcoming_shows = db.Column(db.Integer, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    
    genres = db.Column(db.ARRAY(db.String()), nullable=True, default=[])
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    website_link = db.Column(db.String())
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)    
    seeking_description = db.Column(db.String()) 
    # artists = db.relationship('Artist', secondary=shows_venues_artists,backref=db.backref('venues', lazy=True))
    artists = db.relationship("Show", back_populates="venue")

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # state = db.Column(db.String())
    # city = db.Column(db.String(), nullable=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    
    genres = db.Column(db.ARRAY(db.String()), nullable=True, default=[])
    # address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    website_link = db.Column(db.String())
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)    
    seeking_description = db.Column(db.String()) 
    venues = db.relationship("Show", back_populates="artist")

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

# ERROR [flask_migrate] Error: Target database is not up to date.
# solution : flask db stamp head
# https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date

# SyntaxError: invalid syntax
# >>> from models import * 
# >>> cls
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'cls' is not defined
# >>> clear
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'clear' is not defined
# >>> from app import db
# >>> venue = Venue.query.get(1)                  
# >>> artist = Artist.query.get(2)                   
# >>> show = Show(start_time="2022-08-12") 
# >>> show.artist = artist
# >>> shw.venue = venue
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'shw' is not defined
# >>> show.venue = venue 
# >>> db.sessions.add(show)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'SQLAlchemy' object has no attribute 'sessions'
# >>> db.session.add(show)  
# >>> db.session.commit()
# >>> 