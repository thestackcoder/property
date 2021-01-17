import React, { Component } from "react";
import { render } from "react-dom";

class Project extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/projects")
        .then(response => {
            if (response.status > 400) {
                return this.setState(() => {
                    return { placeholder: "Something went wrong!" };
                });
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
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
        <h1>
            Project's count: {this.state.data.count}
        </h1>
    );
  }
}

export default Project;
