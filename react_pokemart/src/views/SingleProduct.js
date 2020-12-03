import React, { Component } from 'react';
import Pokemon from '../components/Pokemon';

export default class SingleProduct extends Component {
    constructor() {
        super();

        this.state = {
            products: []
        }
    }

    componentDidMount() {
        this.setState({
            products: this.props.currentProduct
        })
    }
    render() {

        return (
            <React.Fragment>
                <div className="card-deck">
                    {this.state.products.map(p => <Pokemon key={p.id} product={p} addToCart={this.props.addToCart} changeCurrentProduct={this.props.changeCurrentProduct}/>)}
                </div>
            </React.Fragment>
            );
         }
    }