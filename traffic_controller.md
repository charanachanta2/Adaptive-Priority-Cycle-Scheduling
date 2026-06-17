# Traffic Controller

## Purpose

The Traffic Controller module serves as the central management unit of the Adaptive Priority Cycle Scheduling (APCS) system.

It is responsible for:

- Executing normal APCS traffic scheduling.
- Monitoring emergency vehicle detection events.
- Interrupting current signal cycles when necessary.
- Generating emergency-priority signal cycles.
- Resuming normal APCS operation after emergency clearance.

---

## Module Architecture

```text
Traffic Controller
│
├── APCS Algorithm
│ ├── Density Calculation
│ ├── Priority Calculation
│ ├── Cycle Generation
│ └── Green Time Allocation
│
├── Emergency Detection
│ ├── Ambulance Detection
│ ├── Fire Truck Detection
│ └── Police Vehicle Detection
│
└── Signal Management
├── Normal APCS Cycle
└── Emergency Override Cycle
```

---

## Normal Operation

The Traffic Controller performs the following steps:

1. Receive vehicle counts from all directions.
2. Calculate traffic density.
3. Calculate APCS priorities.
4. Generate the optimal signal cycle.
5. Allocate green signal times.
6. Update waiting counters.
7. Start the next cycle.

---

## Emergency Override Operation

When an emergency vehicle is detected:

1. Stop current cycle generation.
2. Identify the direction of the emergency vehicle.
3. Assign maximum priority to that direction.
4. Generate a new emergency cycle.
5. Immediately provide a green signal.
6. Allow the emergency vehicle to pass.
7. Return to APCS scheduling.

---

## Dependencies

### APCS_algorithm.py

Provides:

- Vehicle density calculations
- Priority calculations
- Signal cycle generation
- Green time allocation
- Waiting counter management

### Future Modules

- emergency_detection.py
- camera_detection.py
- yolo_detector.py
- signal_controller.py

---

## Future Improvements

### Camera Integration

Emergency vehicle direction will be automatically determined using:

- CCTV Cameras
- OpenCV
- YOLO Object Detection

### Real-Time Monitoring

The controller will support:

- Live traffic density analysis
- Automatic cycle regeneration
- Smart traffic management

### Smart City Integration

The controller can be integrated with:

- Traffic Management Centers
- Emergency Response Systems
- IoT Sensors
- Smart Signal Infrastructure

---

## Conclusion

The Traffic Controller acts as the decision-making layer of the APCS system. It ensures efficient traffic flow during normal operation and provides immediate priority to emergency vehicles through dynamic cycle regeneration and signal override mechanisms.
