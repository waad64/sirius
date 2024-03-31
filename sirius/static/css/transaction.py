form {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
    height: 300px;
    background-color: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(10px);
    padding: 30px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  }
  a:hover{
	color:#4680C7;
}
.form-group{
    align-items: center;
    display: block;
}

.btn{
	display: block;
	width: 50%;
	height: 50px;
	border-radius: 25px;
	outline: none;
	border: none;
	background-image: linear-gradient(to right, #4680C7,#4882ca, #4782ca);
	background-size: 200%;
	font-size: 1.2rem;
	color: #fff;
	font-family: 'Poppins', sans-serif;
	text-transform: capitalize;
	margin: 1rem 0;
	cursor: pointer;
	transition: .5s;
}
.btn:hover{
	background-position: right;
}
.from-group{
    padding:15px;
    text-align: center;
    display: block;
}
.i{
	color: #585555;
	display: flex;
	justify-content: center;
	align-items: center;
}


.i i{
	transition: .3s;
}