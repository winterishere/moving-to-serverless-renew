<template>
  <div>
    <v-app-bar
      app
      clipped-left
    >
      <v-toolbar flat>
        <v-toolbar-title>
          <v-icon>mdi-image-plus</v-icon>
          <strong>CloudAlbum</strong>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="moveToUpload">
              <v-icon>mdi-cloud-upload</v-icon>
            </v-btn>
          </template>
          <span>Upload</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="moveToList">
              <v-icon>mdi-format-list-bulleted-square</v-icon>
            </v-btn>
          </template>
          <span>List</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="moveToMap">
              <v-icon>mdi-map-marker</v-icon>
            </v-btn>
          </template>
          <span>Map</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on" @click="signOut">
              <v-icon>mdi-logout</v-icon>
            </v-btn>
          </template>
          <span>Sign-out</span>
        </v-tooltip>
      </v-toolbar>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: 'LayoutHeader',
  methods: {
    moveToUpload() {
      this.$router.push({ name: 'upload' })
        .catch((err) => {
          if (err.name === 'NavigationDuplicated') {
            // eslint-disable-next-line no-console
            console.info(err);
            return;
          }
          // eslint-disable-next-line no-console
          console.error(err);
        });
    },
    moveToList() {
      this.$router.push({ name: 'photolist' })
        .catch((err) => {
          if (err.name === 'NavigationDuplicated') {
            // eslint-disable-next-line no-console
            console.info(err);
            return;
          }
          // eslint-disable-next-line no-console
          console.error(err);
        });
    },
    moveToMap() {
      this.$router.push({ name: 'map' })
        .catch((err) => {
          if (err.name === 'NavigationDuplicated') {
            // eslint-disable-next-line no-console
            console.info(err);
            return;
          }
          // eslint-disable-next-line no-console
          console.error(err);
        });
    },
    signOut() {
      this.$router.push({ name: 'signout' })
        .catch((err) => {
          if (err.name === 'NavigationDuplicated') {
            // eslint-disable-next-line no-console
            console.info(err);
            return;
          }
          // eslint-disable-next-line no-console
          console.error(err);
        });
    },
  },
};
</script>

<style scoped>

</style>
