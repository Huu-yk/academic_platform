<template>
    <div class="testpage2">
      <div class='calendar_box'>
        <div id='calendar' class='calendar'></div>
      </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {

        }
    },
    computed: {

    },
    methods: {

    },
    mounted() {
        $('#calendar').fullCalendar({
          dayClick: function() {
              alert('a day has been clicked!');
          }
        })
    }
}
</script>
<style>
  .calendar_box {
    width: 80%;
    height: 70%;
    margin: 0 100px;
  }
</style>
