<template>
  <div class="body">
    <!-- <pre>{{ $data }}</pre> -->
    <FlashMessage :position="'top'" />
    <h1 class="page-title">Pick team</h1>
    <div id="team_selection">
      <div id="transfer_field">
        <div class="goalkeeper">
          <!-- Render two placeholders -->
          <div
            v-for="i in [0, 1]"
            :key="i"
            class="player-details"
            :class="{ active: selected[0] == i && selected[1] == 'gk' }"
            @click="toggleActive($event, i, 'gk')"
          >
            <!-- Set selectedPlayerIndex when clicked -->
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="
                myTeam.goalkeeper[i]
                  ? require('@/assets/img/jerseys/' +
                      myTeam.goalkeeper[i].department +
                      '.png')
                  : require('@/assets/img/jerseys/placeholdershirt.png')
              "
              alt=""
            />
            <div class="details">
              <span>GK</span>
              <!-- Check if any selected players in myTeam -->
              <!-- If so display name -->
              <p v-if="myTeam.goalkeeper[i]">
                {{ myTeam.goalkeeper[i].fname }}
              </p>
            </div>
          </div>
        </div>
        <div class="defender">
          <!-- Render three placeholders -->
          <div
            v-for="i in [0, 1, 2]"
            :key="i"
            class="player-details"
            :class="{ active: selected[0] == i && selected[1] == 'df' }"
            @click="toggleActive($event, i, 'df')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="
                myTeam.defender[i]
                  ? require('@/assets/img/jerseys/' +
                      myTeam.defender[i].department +
                      '.png')
                  : require('@/assets/img/jerseys/placeholdershirt.png')
              "
              alt=""
            />
            <div class="details">
              <span>DEF</span>
              <p v-if="myTeam.defender[i]">{{ myTeam.defender[i].fname }}</p>
            </div>
          </div>
        </div>
        <div class="midfielder">
          <div
            v-for="i in [0, 1, 2]"
            :key="i"
            class="player-details"
            :class="{ active: selected[0] == i && selected[1] == 'md' }"
            @click="toggleActive($event, i, 'md')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="
                myTeam.midfielder[i]
                  ? require('@/assets/img/jerseys/' +
                      myTeam.midfielder[i].department +
                      '.png')
                  : require('@/assets/img/jerseys/placeholdershirt.png')
              "
              alt=""
            />
            <div class="details">
              <span>MID</span>
              <p v-if="myTeam.midfielder[i]">
                {{ myTeam.midfielder[i].fname }}
              </p>
            </div>
          </div>
        </div>
        <div class="striker">
          <div
            v-for="i in [0, 1]"
            :key="i"
            class="player-details"
            :class="{ active: selected[0] == i && selected[1] == 'st' }"
            @click="toggleActive($event, i, 'st')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="
                myTeam.striker[i]
                  ? require('@/assets/img/jerseys/' +
                      myTeam.striker[i].department +
                      '.png')
                  : require('@/assets/img/jerseys/placeholdershirt.png')
              "
              alt=""
            />
            <div class="details">
              <span>ST</span>
              <p v-if="myTeam.striker[i]">{{ myTeam.striker[i].fname }}</p>
            </div>
          </div>
        </div>
      </div>
      <div id="transfer_sidebar" class="sidebar">
        <!-- Show if server status is false or down -->
        <h2 v-if="!serverStatus">Server could not be reached.</h2>
        <div id="info">
          <h1>{{ myTeamName }}</h1>
        </div>
        <div class="skewed">
          <div
            v-for="(player, index) in playersApi"
            :key="index"
            :class="checkSelected(player) ? 'disabled' : ''"
            class="player-options"
          >
            <img
              @click="getPlayers($event, i)"
              class="i sidebar-img"
              :src="
                require('@/assets/img/jerseys/' + player.department + '.png')
              "
              alt=""
            />
            <p class="player-name">{{ player.fname }}</p>
            <button
              @click="addPlayer($event, player)"
              :disabled="checkSelected(player)"
              class="player-options-add"
            >
              Add
            </button>
          </div>
        </div>
        <div class="submit-button-container">
          <button @click="submit" class="team-submit-button">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // Stores users selection
      myTeam: {
        goalkeeper: [null, null],
        defender: [null, null, null],
        midfielder: [null, null, null],
        striker: [null, null],
      },

      myTeamName: "",

      // Players from api based on position
      playersApi: [],

      // Server status Up == True
      serverStatus: true,

      // Player being replaced in myTeam.<position>
      selectedPlayerIndex: null,

      // Active player order number and playing position
      selected: [],

      teamCounter: {
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
      },
    };
  },

  methods: {
    // Get Access Token
    get_access_token: function () {
      // Get Token from Local Storage
      let access_token = sessionStorage.getItem("token");

      // Prepare a header config
      let config = {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      };
      return config;
    },
    // Get players from API
    getPlayers(e, selectedPlayerIndex) {
      const position = e.path[2].className;
      // console.log(e.path);
      let config = this.get_access_token();
      axios
        .get("http://localhost:5000/getplayers/" + position, config)
        .then((res) => {
          this.playersApi = res.data.players;
          this.serverStatus = true;
          this.selectedPlayerIndex = selectedPlayerIndex;
        })
        .catch((err) => {
          this.serverStatus = false;
          console.error(err);
        });
    },

    // Add selected player to myTeam based on position
    addPlayer(e, player) {
      this.teamCounter[player.dept_id] += 1;
      // Check team limit
      if (this.teamCounter[player.dept_id] > 3) {
        this.teamCounter[player.dept_id] -= 1;
        this.flashMessage.error({message: "Can not pick more than three players from the same team!"});
        return;
      }
      this.$set(this.myTeam[player.position], this.selectedPlayerIndex, player);
    },

    // Check if player is in myTeam.<position>
    checkSelected(player) {
      let check = false;
      this.myTeam[player.position].filter(function (myPlayer) {
        if (myPlayer && myPlayer.id == player.id) check = true;
      });

      return check;
    },

    // Add active player to selected
    toggleActive(e, playerNo, playerPos) {
      this.$set(this.selected, 0, playerNo);
      this.$set(this.selected, 1, playerPos);
    },

    submit() {
      // Check for if team is complete
      let teamCompleted = true;
      for (const position in this.myTeam) {
        for (const player of this.myTeam[position]) {
          teamCompleted = !player ? false : true;
        }
      }

      if (teamCompleted) {
        this.$store.commit("updateMyTeam", this.myTeam);
        this.$router.push("/registration");
        return;
      }

      alert("You need to complete your team before registration!");
    },
  },

  created() {
    this.myTeamName = this.$store.state.myTeamName;

    axios
      .get("http://localhost:5000/getteam/" + this.$store.state.userId + "/5")
      .then((res) => {
        // Check if user has picked team
        if (res.data.team.length != 0) this.$router.push("/myteam");
      })
      .catch((err) => console.error(err));
  },
};
</script>

<style scoped>
@import "../assets/css/sidebar.css";

* {
  box-sizing: border-box;
}

body {
  overflow-y: scroll;
  font-family: futura-pt;
}

.body {
  min-height: 100vh;
  background: url("../assets/img/epic_waves.jpg");
}

.page-title {
  color: var(--secondary-color);
  padding: 2% 0 0;
  text-align: center;
  font-size: 3rem;
  font-family: limelight;
  margin-bottom: -1%;
}

#team_selection {
  padding: 2% 7%;
  display: grid;
  grid-template-columns: 3fr 1fr;
  grid-column-gap: 2rem;
  width: 100%;
  min-height: 100%;
}

#transfer_field {
  padding: 2% 0;
  display: grid;
  grid-template-rows: repeat(4, 150px);
  grid-gap: 1rem;
  background-image: url("../assets/img/fields/Field4.0.png"),
    url("../assets/img/field-background.jpg");
  background-repeat: no-repeat;
  animation: rise 1s forwards;
}

@keyframes rise {
  0% {
    background-position: 50% -50%;
  }
  100% {
    background-position: 50%;
  }
}

#transfer_field > div {
  display: flex;
  justify-content: center;
}

#transfer_field > div > div > img {
  display: block;
}

#info {
  color: var(--secondary-color);
}

div.disabled {
  pointer-events: none;
  opacity: 0.7;
}

.active {
  border-radius: 10%;
  background: url("../assets/img/epic_waves.jpg");
  animation: pop 0.4s forwards;
}

@keyframes pop {
  0% {
    margin: 0;
  }
  100% {
    margin: 10px 10px 0;
  }
}

.starting_team div,
.substitutes div {
  position: relative;
}

.player-details {
  position: relative;
  text-align: center;
}

.details {
  position: absolute;
  bottom: -10px;
  left: 0;
  right: 0;
  margin: 0 auto;
  text-align: center;
  width: 100px;
}

#team_selection .player-details img {
  width: 200px;
  cursor: pointer;
}

.details > span {
  display: block;
  background-color: var(--accent-color);
  color: var(--secondary-color);
}

.details > p {
  background-color: var(--secondary-color);
  color: var(--accent-color);
}

.player-options {
  display: grid;
  grid-template-columns: 20px 3fr 50px;
  grid-column-gap: 1em;
  padding: 0 10%;
  align-content: center;
  background: var(--secondary-color);
  margin-bottom: 5%;
}

.player-options * {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: montserrat-light;
  color: var(--primary-color);
}

.player-name {
  overflow-wrap: break-word;
  word-wrap: break-word;
}

.player-options button {
  font-family: futura-pt;
  /* border-radius: solid thin; */
  outline: none;
  border-top: none;
  border-bottom: none;
  background: var(--accent-color);
  color: var(--secondary-color);
}

.sidebar-img {
  width: 50px;
}

.submit-button-container {
  position: relative;
  margin-top: 30px;
}

.team-submit-button {
  font-size: 1.5rem;
  letter-spacing: 0.8px;
  width: 100%;
  padding: 2% 0;
  margin-bottom: 10%;
  position: relative;
  border: 1px solid black;
  border-radius: 0 0 5px 5px;
  /* background: var(--primary-color); */
  color: var(--primary-color);
}

.team-submit-button:after {
  content: "";
  width: 100%;
  height: 5px;
  background: linear-gradient(
    40deg,
    #dc143c,
    #e22f72,
    #c071c7,
    #8d9fed,
    #78b0f6,
    #5ffbf1
  );
  background-size: 400%;
  position: absolute;
  /* z-index: -1; */
  top: 99%;
  left: 0;
  border-radius: inherit;
  animation: glimmer 20s infinite alternate;
}

.team-submit-button:active {
  transform: translateY(5px);
}

.team-submit-button:active:after {
  width: 0;
}

@keyframes glimmer {
  0% {
    background-position: 0;
  }
  100% {
    background-position: 100%;
  }
}
</style>
