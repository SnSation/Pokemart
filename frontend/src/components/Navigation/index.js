import React, { Component } from 'react';
import './navigation.css';
import { Link } from 'react-router-dom';

export default class Navigation extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light">
                <Link className="navbar-brand" to="/">PokeMart</Link>
                <button className="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#collapsibleNavId" aria-controls="collapsibleNavId"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="collapsibleNavId">
                    <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li className="nav-item active">
                            <Link className="nav-link" to="/store">Store</Link>
                        </li>
                        <li className="nav-item dropdown">
                            <Link className="nav-link dropdown-toggle text-dark" to="#" id="shopDrop" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Categories</Link>
                                <div className="dropdown-menu" aria-labelledby="dropdownId">
                                    <Link className="dropdown-item" to="#">Items</Link>
                                    <Link className="nav-link dropdown-toggle text-dark" to="#" id="pokemonDrop" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Pokemon</Link>
                                        <div className="dropdown-menu" aria-labelledby="dropdownId">
                                            <Link className="dropdown-item" to="#">Global</Link>
                                            <Link className="dropdown-item" to="#">Kanto</Link>
                                            <Link className="dropdown-item" to="#">Johto</Link>
                                            <Link className="dropdown-item" to="#">Sinnoh</Link>
                                            <Link className="dropdown-item" to="#">Unova</Link>
                                            <Link className="dropdown-item" to="#">Alola</Link>
                                        </div>
                                </div>
                        </li>
                        <li className="nav-item active bg-dark">
                            <Link className="nav-link text-white" to="/cart">Cart: {`${this.props.cart.length}`} | $0 </Link>
                        </li>
                    </ul>
                </div>
            </nav>
        );
    }
}