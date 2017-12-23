<template>
    <div class="testpage1">
      <full-calendar :events="fcEvents"
                    locale="en"
                    @eventClick="eventClick"
                    @dayClick="dayClick"
                    @moreClick="moreClick"
      >

      </full-calendar>
    </div>
</template>

<script>
let demoEvents = [
    {
      title    : 'Sunny 725-727',
      start    : '2017-02-25',
      end      : '2017-02-27',
      cssClass : 'family'
    },
    {
      title : 'Lunfel 726-727',
      start : '2017-02-26',
      end : '2017-02-27',
      cssClass : ['home', 'work']
    },
    {
      title : 'Lunfel 2/27-2/28',
      start : '2017-02-27',
      end : '2017-02-28'
    },
    {
        title : 'Lunfel 2/27-2/28',
        start : '2017-02-27',
        end : '2017-02-28'
    },
    {
        title : 'Lunfel 2/27-2/28',
        start : '2017-02-27',
        end : '2017-02-28'
    },
    {
        title : 'Lunfel 2/26-3/05',
        start : '2017-02-26',
        end : '2017-03-05'
    },
    {
        title : 'Lunfel 1/27-1/28',
        start : '2017-01-27',
        end : '2017-01-28'
    },
    {
        title : 'Lunfel 1/27-2/2',
        start : '2017-11-27',
        end : '2017-12-02'
    },
    {
        title : 'Lunfel 3/27-3/28',
        start : '2017-11-27',
        end : '2017-11-28'
    },
  ];
export default {
  data () {
		return {
            name:'Sunny!',
            fcEvents : demoEvents
        }
	},
  methods : {
    /*'changeMonth' (start, end, current) {
      console.log('changeMonth', start.format(), end.format(), current.format())
    },*/
    'eventClick' (event, jsEvent, pos) {
       console.log('eventClick', event, jsEvent, pos)
    },
    'dayClick' (day, jsEvent) {
      console.log('dayClick', day, jsEvent)
    },
    'moreClick' (day, events, jsEvent) {
      console.log('moreCLick', day, events, jsEvent)
    }
  },
  components : {
	'full-calendar': require('vue-fullcalendar')
  }
}
</script>
