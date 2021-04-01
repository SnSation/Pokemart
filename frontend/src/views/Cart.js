import React, { Component } from 'react';
import CartItem from '../components/CartItem';

export default class Cart extends Component {
    constructor() {
        super();

        this.state  = {
            uniqueItems : []
        }
    }

    componentDidMount() {
        this.setState({
            uniqueItems : [...new Set(this.props.cart)]
        })
    }


    render() {
        return (
            <React.Fragment>
                <div className="card-deck">
                    {this.state.uniqueItems.map(p => <CartItem key={p.id} product={p} removeFromCart={this.props.removeFromCart} />)}
                </div>
            </React.Fragment>
        );
    }
}