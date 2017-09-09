import React from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';

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