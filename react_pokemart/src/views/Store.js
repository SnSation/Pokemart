import React, { Component } from 'react';
import Pokemon from '../components/Pokemon';

export default class Store extends Component {
    constructor() {
        super();

        this.state = {
            products: []
        }
    }

    componentDidMount(){
        console.log("Mounted");
        fetch('http://127.0.0.1:5000/national_dex')
            .then(response => response.json())
            .then(data => this.setState({ products: data }))
            .catch(error => console.error(error));
        
        console.log(this.state.products)
    }


    render() {
        return (
            <React.Fragment>
                <div className="card-deck">
                    {this.state.products.map(p => <Pokemon key={p.id} product={p} addToCart={this.props.addToCart} changeCurrentProduct={this.props.changeCurrentProduct} />)}
                </div>
            </React.Fragment>
        );
    }
}