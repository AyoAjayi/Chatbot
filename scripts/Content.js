import * as React from 'react';
import { Socket } from './Socket';
import GoogleLogin from 'react-google-login';
/*global gapi*/
//

export class Content extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data_received: []};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleChange(event) {
    this.setState({value: event.target.value});
  }
  
  handleSubmit(event) {
      Socket.emit('new_data', 
      {'data':this.state.value,
        'url': this.state.url
      });
      event.preventDefault();
      console.log(this.state.data_received);
      console.log(this.state.data_received[0]);
      
  }
  componentDidMount() {
        Socket.on('data received', (message) => {
            this.setState({
                'data_received': message['data'],

            });
        });
        Socket.on('url received', (url) => {
            this.setState({
                'url_received': url['data'],
        });

      });
    }

  render() {
    const responseGoogle = (response) => {
        let auth = gapi.auth2.getAuthInstance();
        let user = auth.currentUser.get();
        if (user.isSignedIn()) {
            console.log("google token" + user.getAuthResponse().id_token);
        }
       this.setState({username: response});
        Socket.emit('login', 
            {'username': this.state.username
        },
        );
       
    console.log(response);
    };
    // let output = this.state.data_received.map((f, index) => <div><li style={{ border: "20px solid azure" }}key={index}>{f} </li></div>);
    
    let url = this.state.url_received;
    return (
      <div style={{ backgroundColor: "white", border: "20px solid purple"}}>
        <h2 style={{ padding: "10px", textAlign: "center", color: "deepskyblue"}}>Ayo's Chatbot</h2>
        <ul>
            { this.state.data_received.map( name_message =>
              <li key = {name_message[0].id} className = "message-with-image">
                <img src={name_message[2]} alt = "User Image"></img>
                <div>
                  <h5> {name_message[0]}</h5>
                  <p> {name_message[1]} </p>
                </div>
              </li> )}
        </ul>
        <a href={url}>{url}</a>
         <form onSubmit={this.handleSubmit} style={{width: "600px", height: "200px"}}>
            <label>
              <textarea rows="10" columns= "100" postion="relative" value={this.state.value} onChange={this.handleChange}></textarea>
            </label>
          <input type="submit" style ={{width: "2200", height:"1250", color: "blue", fontSize: "95px"}} value="Send" />
        </form>
        <GoogleLogin
        clientId = '412518169761-vo15jqtbrgcbg30d9t690qc3odu17gk0.apps.googleusercontent.com'
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
        />
      </div>
    );
  }
}






















// import * as React from 'react';
// import { Socket } from './Socket';
// import GoogleLogin from 'react-google-login';
// /*global gapi*/

// export class Content extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {data_received: [],
//     };
//     this.handleChange = this.handleChange.bind(this);
//     this.handleSubmit = this.handleSubmit.bind(this);
//   }
  
//   handleChange(event) {
//     this.setState({value: event.target.value});
//   }
  
//   //sending to the server
//   handleSubmit(event) {
//       Socket.emit('new_data', 
//       {'data':this.state.value,
//         'url': this.state.url
//       });
//       event.preventDefault();
//       console.log(this.state.data_received);
//   }
//   //receiving from the client
//   componentDidMount() {
//         Socket.on('data received', (message) => {
//             this.setState({
//                 'data_received': message,
//             });
//         });
        
//         Socket.on('url received', (url) => {
//             this.setState({
//                 'url_received': url['data'],});
//         });
//       }

//   render() {
//     console.log(this.state.data_received);
//     const responseGoogle = (response) => {
//         let auth = gapi.auth2.getAuthInstance();
//         let user = auth.currentUser.get();
//         if (user.isSignedIn()) {
//             console.log("google token" + user.getAuthResponse().id_token);
//         }
//         this.setState({username: response});
//         Socket.emit('login', 
//             {'username': this.state.username
//         },
//         );
//     console.log(response);
//     };
//     // let final_messages = this.state.data_received;
    
    
    
//     // let output = this.state.data_received.map((f, index) => {console.log(f)}); //<div><li style={{ border: "20px solid azure" }}key={this.state.data_received[0].id}>{f} </li></div>);
//     // let chats = this.state.data_received
//     // let output = chats.map((l,index) => {console.log(l)})
//     // let output = this.state.data_received.map((f, index) => <div><li style={{ border: "20px solid azure" }}key={this.state.data_received[0].id}>{f} </li></div>);
//     let output = this.state.data_received.map((f, index) => <li key={this.state.data_received[0].id}>{f} </li>);
//     let url = this.state.url_received;
//     console.log(output);
    
//     return (
//       <div style={{ backgroundColor: "white", border: "20px solid purple"}}>
//         <h2 style={{ padding: "10px", textAlign: "center", color: "deepskyblue"}}>Ayo's Chatbot</h2>
//         <a href={url}>{url}</a>
      
//         <form onSubmit={this.handleSubmit} style={{width: "600px", height: "200px"}}>
//             <label>
//               <textarea rows="10" columns= "100" postion="relative" value={this.state.value} onChange={this.handleChange}></textarea>
//             </label>
//           <input type="submit" style ={{width: "2200", height:"1250", color: "blue", fontSize: "95px"}} value="Send" />
//         </form>
//         <GoogleLogin
//             clientId = '412518169761-vo15jqtbrgcbg30d9t690qc3odu17gk0.apps.googleusercontent.com'
//             buttonText="Login"
//             onSuccess={responseGoogle}
//             onFailure={responseGoogle}
//             cookiePolicy={'single_host_origin'}
//         />
        
//         <ul>{output}</ul>
//       </div>
//     );
//   }
// }
































// import * as React from 'react';
// import { Socket } from './Socket';
// import GoogleLogin from 'react-google-login';
// /*global gapi*/

// export class Content extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {data_received: [],
//     };
//     this.handleChange = this.handleChange.bind(this);
//     this.handleSubmit = this.handleSubmit.bind(this);
//   }
  
//   handleChange(event) {
//     this.setState({value: event.target.value});
//   }
  
//   //sending to the server
//   handleSubmit(event) {
//       Socket.emit('new_data', 
//       {'data':this.state.value,
//         'url': this.state.url
//       });
//       event.preventDefault();
//       console.log(this.state.data_received);
//   }
//   //receiving from the client
//   componentDidMount() {
//         Socket.on('data received', (message) => {
//             this.setState({
//                 'data_received': message[0],
//                 'username_received': message[1],
//                 'image_received': message[2]
            
//             });
//             console.log(this.state.data_received);
//             console.log(this.state.username_received);
//             console.log(this.state.image_received);
//         });
        
//         Socket.on('url received', (url) => {
//             this.setState({
//                 'url_received': url['data'],});
//         });
//       }

//   render() {
//     const responseGoogle = (response) => {
//         let auth = gapi.auth2.getAuthInstance();
//         let user = auth.currentUser.get();
//         if (user.isSignedIn()) {
//             console.log("google token" + user.getAuthResponse().id_token);
//         }
//         this.setState({username: response});
//         Socket.emit('login', 
//             {'username': this.state.username
//         },
//         );
//     console.log(response);
//     };
//     let output = this.state.data_received.map((f, index) => <div><li style={{ border: "20px solid azure" }}key={this.state.data_received[0].id}>{f} </li></div>);
//     // let output = this.state.data_received;
//     let url = this.state.url_received;
//     let name = this.state.username_received;
//     let image = this.state.image_receieved;
    
//     return (
//       <div style={{ backgroundColor: "white", border: "20px solid purple"}}>
//         <h2 style={{ padding: "10px", textAlign: "center", color: "deepskyblue"}}>Ayo's Chatbot</h2>
//         <ul>{output}</ul>
//         <a href={url}>{url}</a>
//         { name }
//         { image }
//         <form onSubmit={this.handleSubmit} style={{width: "600px", height: "200px"}}>
//             <label>
//               <textarea rows="10" columns= "100" postion="relative" value={this.state.value} onChange={this.handleChange}></textarea>
//             </label>
//           <input type="submit" style ={{width: "2200", height:"1250", color: "blue", fontSize: "95px"}} value="Send" />
//         </form>
//         <GoogleLogin
//             clientId = '412518169761-vo15jqtbrgcbg30d9t690qc3odu17gk0.apps.googleusercontent.com'
//             buttonText="Login"
//             onSuccess={responseGoogle}
//             onFailure={responseGoogle}
//             cookiePolicy={'single_host_origin'}
//         />
//       </div>
//     );
//   }
// }
























































// import * as React from 'react';
// import { Socket } from './Socket';
// import GoogleLogin from 'react-google-login';
// /*global gapi*/

// export class Content extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {data_received: [],
//                   username_received: '',
//                   image_receieved: ''
//     };
//     this.handleChange = this.handleChange.bind(this);
//     this.handleSubmit = this.handleSubmit.bind(this);
//   }
  
//   handleChange(event) {
//     this.setState({value: event.target.value});
//   }
  
//   //sending to the server
//   handleSubmit(event) {
//       Socket.emit('new_data', 
//       {'data':this.state.value,
//         'url': this.state.url
//       });
//       event.preventDefault();
//       console.log(this.state.data_received);
//   }
//   //receiving from the client
//   componentDidMount() {
//         Socket.on('data received', (message) => {
//             this.setState({
//                 'data_received': message[0],
//                 'username_received': message[1],
//                 'image_received': message[2]
            
//             });
//             console.log(this.state.data_received);
//             console.log(this.state.username_received);
//             console.log(this.state.image_received);
//         });
        
//         Socket.on('url received', (url) => {
//             this.setState({
//                 'url_received': url['data'],});
//         });
//       }

//   render() {
//     const responseGoogle = (response) => {
//         let auth = gapi.auth2.getAuthInstance();
//         let user = auth.currentUser.get();
//         if (user.isSignedIn()) {
//             console.log("google token" + user.getAuthResponse().id_token);
//         }
//         this.setState({username: response});
//         Socket.emit('login', 
//             {'username': this.state.username
//         },
//         );
//     console.log(response);
//     };
//     let output = this.state.data_received.map((f, index) => <div><li style={{ border: "20px solid azure" }}key={this.state.data_received[0].id}>{f} </li></div>);
//     // let output = this.state.data_received;
//     let url = this.state.url_received;
//     let name = this.state.username_received;
//     let image = this.state.image_receieved;
    
//     return (
//       <div style={{ backgroundColor: "white", border: "20px solid purple"}}>
//         <h2 style={{ padding: "10px", textAlign: "center", color: "deepskyblue"}}>Ayo's Chatbot</h2>
//         <ul>{output}</ul>
//         <a href={url}>{url}</a>
//         { name }
//         { image }
//         <form onSubmit={this.handleSubmit} style={{width: "600px", height: "200px"}}>
//             <label>
//               <textarea rows="10" columns= "100" postion="relative" value={this.state.value} onChange={this.handleChange}></textarea>
//             </label>
//           <input type="submit" style ={{width: "2200", height:"1250", color: "blue", fontSize: "95px"}} value="Send" />
//         </form>
//         <GoogleLogin
//             clientId = '412518169761-vo15jqtbrgcbg30d9t690qc3odu17gk0.apps.googleusercontent.com'
//             buttonText="Login"
//             onSuccess={responseGoogle}
//             onFailure={responseGoogle}
//             cookiePolicy={'single_host_origin'}
//         />
//       </div>
//     );
//   }
// }






























