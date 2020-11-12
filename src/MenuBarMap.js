import React, { Component } from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const mapStyles = {
  width: '100%',
  height: '100%',
  lat: -1.2884,
  lng: 36.8233
};

export class ManuBarMap extends Component {
    state = {userLocation: { lat: 32, lng: 32 }, 
            loading: true };

    componentDidMount(props) {
      navigator.geolocation.getCurrentPosition(
        position => {
          const { latitude, longitude } = position.coords;
  
          this.setState({
            userLocation: { lat: latitude, lng: longitude },
            loading: false
          });
        },
        () => {
          this.setState({ loading: false });
        }
      );
    }
  
  render() {
    const { loading, userLocation } = this.state;
    // const { google } = this.props;

    if (loading) {
      return null;
    }
    return (
      <Map
        google={this.props.google}
        zoom={16}
        style={mapStyles}
        initialCenter={userLocation}>
          <Marker onClick={this.onMarkerClick}
                name={'Current location'} />
        </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: 'AIzaSyCba5Z2xaqw3zNZcgis6h01iFbwzjy7-hk'
})(ManuBarMap);