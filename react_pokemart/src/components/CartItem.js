import React, { Component } from 'react';

export default class CartItem extends Component {
    render() {
        const p = this.props.product;

        return (
            <div className="col-md-4">
                <div className="card">
                    <div className="card-body">
                        <h4 className="card-title">
                            {p.name}
                            <span className="float-right">{`$${p.price}`}</span>    
                        </h4>
                        <img src={p.sprite} alt={p.name} className="img-fluid" />
                        <hr />
                        <p className="card-text">{p.types[0]} {p.types[1] == null ? p.types[1]:` | ${p.types[1]}`}</p>
                        <p className="card-text">{`Height: ${p.height} | Weight: ${p.weight}`}</p>
                        <hr />
                        <button className="btn btn-outline-success btn-block" onClick={() => this.props.removeFromCart(p)}>Remove From Cart</button>
                    </div>
                </div>
            </div>
        );
    }
}