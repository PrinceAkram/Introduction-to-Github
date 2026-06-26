# Fundamentals of Electromagnetics

A comprehensive guide to the physics, equations, and applications of electromagnetic fields and wave theory.

---

## 1. Core Vector Calculus & Mathematical Foundations
Electromagnetics relies heavily on vector calculus to describe how fields change across space and time.

* **Gradient ($\nabla f$):** Represents the rate and direction of maximum increase of a scalar field (e.g., electric potential).
* **Divergence ($\nabla \cdot \mathbf{A}$):** Measures the magnitude of a vector field's source or sink at a given point (how much the field spreads out).
* **Curl ($\nabla \times \mathbf{A}$):** Measures the rotation or "swirl" of a vector field around a point.

---

## 2. Maxwell's Equations
Maxwell's equations form the absolute foundation of classical electromagnetics, predicting everything from static electricity to light waves.

### 1. Gauss's Law for Electricity
Electric charge produces an electric field. The total electric flux through a closed surface is proportional to the enclosed charge.
$$\nabla \cdot \mathbf{D} = \rho_v$$

### 2. Gauss's Law for Magnetism
There are no isolated magnetic charges (monopoles). Magnetic field lines always form continuous, closed loops.
$$\nabla \cdot \mathbf{B} = 0$$

### 3. Faraday's Law of Induction
A time-varying magnetic field creates a circulating electric field (the operating principle behind electric generators).
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial \partial t}$$

### 4. Ampere's Circuital Law (with Maxwell's Correction)
An electric current or a time-varying electric field generates a circulating magnetic field.
$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial \partial t}$$

---

## 3. Electromagnetic Waves & Propagation
When electric and magnetic fields oscillate together, they travel through space as electromagnetic waves (such as light, Wi-Fi, and X-rays).

* **Uniform Plane Waves:** An idealized wave where the electric and magnetic fields are uniform across an infinite plane perpendicular to the direction of travel.
* **Intrinsic Impedance ($\eta$):** The ratio of the electric field to the magnetic field in a medium. For free space/vacuum:
$$\eta_0 \approx 120\pi \approx 377\ \Omega$$
* **Poynting Vector ($\mathbf{S}$):** Represents the directional energy flux density (power per unit area) of an electromagnetic wave.
$$\mathbf{S} = \mathbf{E} \times \mathbf{H}$$

---

## 4. Boundary Conditions & Oblique Incidence
When an electromagnetic wave hits the interface between two different media (like air to glass), it undergoes reflection and transmission.
