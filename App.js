import React from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';
import { Permissions, Notifications } from 'expo';

export default class App extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.header}>
          Period Distress App
        </Text>

        <TextInput
          style={styles.input}
          placeholder="Username"
          clearTextOnFocus={true}
          maxLength={30}
          autoCorrect={false}
          autoCapitalize={'none'}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          clearTextOnFocus={true}
          secureTextEntry={true}
          maxLength={20}
          autoCorrect={false}
        />

        <View style={{ flexDirection: 'row' }}>
          <Button
            title="Login"
            color="#000"
            style={styles.button}
          />
          <Text>           </Text>
          <Button
            title="Sign Up"
            color="#000"
          />
          {/* <TouchableOpacity
            style={styles.button}>
            <Text style={styles.button_text}>Login</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.button}>
            <Text style={styles.button_text}>Sign Up</Text>
          </TouchableOpacity> */}
        </View>
      </View>
    );
  }
}

// _onLogin = async () => {

// }

// async function getUserInfo(accessToken) {
//   let userInfoResponse = await fetch('https://www.googleapis.com/userinfo/v2/me', {
//     headers: { Authorization: `Bearer ${accessToken}`},
//   });

//   return userInfoResponse;
// }

// const PUSH_ENDPOINT = 'https://data.amicably83.hasura-app.io/';

// async function registerForPushNotificationsAsync() {
//   const { existingStatus } = await Permissions.getAsync(Permissions.NOTIFICATIONS);
//   let finalStatus = existingStatus;

//   // only ask if permissions have not already been determined, because
//   // iOS won't necessarily prompt the user a second time.
//   if (existingStatus !== 'granted') {
//     // Android remote notification permissions are granted during the app
//     // install, so this will only ask on iOS
//     const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS);
//     finalStatus = status;
//   }

//   // Stop here if the user did not grant permissions
//   if (finalStatus !== 'granted') {
//     return;
//   }

//   // POST the token to our backend so we can use it to send pushes from there
//   return fetch(PUSH_ENDPOINT, {
//     method: 'POST',
//     headers: {
//       'Accept': 'application/json',
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({
//       token: {
//         value: token,
//        },
//        user: {
//         username: 'Brent',
//        },
//     }),
//   });
// }

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#add8e6',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    fontSize: 30,
    margin: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    alignSelf: 'stretch',
    margin: 25,
    padding: 5,
  },
  button: {
    padding: 30,
  },
});