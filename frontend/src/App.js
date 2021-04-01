import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './views/Home';
import Store from './views/Store';
import Cart from './views/Cart';
import SingleProduct from './views/SingleProduct';

export default class App extends Component {
  constructor() {
    super();

    this.state = {
      cart: [],
      currentProduct: []
    }
  }

  addToCart = (product) => {
    this.setState({
      cart: this.state.cart.concat(product)
    })
  }

  removeFromCart = product => {
    let newCart = [...this.state.cart];

    for (let i = 0; i < newCart.length; i++) {
      const item = newCart[i];
      if (product === item) {
        newCart.splice(i, 1)
        break;
      }
    }

    this.setState({
      cart: newCart
    })
  }

  changeCurrentProduct = product => {
    this.setState({
      currentProduct:[product]
    })
  }

  render() {
    return (
      <div>

        <Navigation cart={this.state.cart}/>

        <div className="container">
          <Switch>
            <Route exact path='/' render={() => <Home />}/>
            <Route path='/store' render={() => <Store addToCart={this.addToCart} changeCurrentProduct={this.changeCurrentProduct} />}/>
            <Route path='/cart' render={() => <Cart cart={this.state.cart} removeFromCart={this.removeFromCart} />} />
            <Route path='/single_product' render={() => <SingleProduct currentProduct={this.state.currentProduct} changeCurrentProduct={this.changeCurrentProduct}/>} addToCart={this.addToCart}/>
          </Switch>
        </div>

      </div>
    );
  }
}