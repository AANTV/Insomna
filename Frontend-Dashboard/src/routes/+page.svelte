<script>
      import {
        Title,
        Tooltip,
        Legend,
        BarElement,
        CategoryScale,
        LinearScale,
    } from 'chart.js';

    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';

    let data1 = [90, 98, 99, 100, 100, 101, 100];
    let labels1= ['1','2', '3', '4', '5', '6', '7'];

    let data2 = [1, 1, 2, 1, 2, 3, 3];
    let labels2= ['8pm','7pm', '9pm', '10pm', '11pm', '12am', '1am'];

    let data3 = [45, 67, 48, 51, 52, 50, 48];
    let labels3= ['8pm','7pm', '9pm', '10pm', '11pm', '12am', '1am'];

    let data4 = [10, 12, 45, 12, 10, 8, 9];
    let labels4= ['A','B', 'D', 'G', 'T', 'A', 'A'];

    let ctx1;
    let ctx2;
    let ctx3;
    let ctx4;
    let canvas1;
    let canvas2;
    let canvas3;
    let canvas4;

    onMount(() => {
        ctx1 = canvas1.getContext('2d');
        var chart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: labels1,
                datasets: [
                    {
                        label: 'Sleep scale',
                        data: data1
                    }
                ]
            }
        });
    });

    onMount(() => {
        ctx2 = canvas2.getContext('2d');
        var chart1 = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: labels2,
                datasets: [
                    {
                        label: 'Hours',
                        data: data2
                    }
                ]
            }
        });
    });

    onMount(() => {
        ctx3 = canvas3.getContext('2d');
        var chart1 = new Chart(ctx3, {
            type: 'bar',
            data: {
                labels: labels3,
                datasets: [
                    {
                        label: 'Rate',
                        data: data3
                    }
                ]
            }
        });
    });

    onMount(() => {
        ctx4 = canvas4.getContext('2d');
        var chart1 = new Chart(ctx4, {
            type: 'line',
            data: {
                labels: labels4,
                datasets: [
                    {
                        label: 'Count',
                        data: data4
                    }
                ]
            }
        });
    });
</script>
  
  <style lang="postcss">
    :global(html) {
      background-color: theme(colors.gray.100);
    }

    canvas {
        width: 100%;
        height: 100%;
        background-color: #666;
    }
  </style>

<div class="px-8 pt-8 grid grid-cols-4 gap-4">
    <div class="p-6 py-9 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 h-96">
        <a href="#">
            <h7 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Last Night Sleep</h7>
        </a>
        <br>
        <h1 class="p-6 py-9 mb-2 text-9xl font-bold tracking-tight text-gray-900 dark:text-white">6 hrs</h1>
       </div>

    <div class="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Snores Count</h5>
        </a>
        <p class="p-6 mb-2 text-9xl font-bold tracking-tight text-gray-900 dark:text-white">20</p>
    </div>
    <div class="col-span-2 p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Weekly Sleep Summary</h5>
        </a>
        <main>
            <canvas bind:this={canvas1} height={300}/>
        </main>
        
    </div>
</div>



<div class="px-8 pt-4 justify-center grid grid-cols-3 gap-4">
    <div class="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 h-96">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Last Nights Sleep Stages</h5>
        </a>
        <main>
            <canvas bind:this={canvas2} height={300}/>
        </main>
        
         </div>

    <div class="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Last Nights Respiration</h5>
        </a>
        <canvas bind:this={canvas3} height={300}/>
        
    </div>
    <div class="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Last Night Brain Activity</h5>
            
        </a>
        <canvas bind:this={canvas4} height={300}/>
    </div>
</div>


