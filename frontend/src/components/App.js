import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        fetch("api/games")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong!" };
                    });
                }
                return response.json();
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <ul>
                {this.state.data.map(game => {
                    return (
                        <h3 key={'game_'+game.id}>
                            {game.id}. {game.type}
                            <ul>
                            {game.players.map(player =>
                                <li key={'player_'+player.id}>
                                    {player.name}
                                </li>)}
                            </ul>
                        </h3>
                    );
                })}
            </ul>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container)