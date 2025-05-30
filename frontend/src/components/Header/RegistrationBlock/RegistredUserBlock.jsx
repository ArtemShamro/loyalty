import React from "react";
import Button from "../../Button/Button";
import "./RegistredUserBlock.css";
import { Logout } from "../../../api/user";
import { AuthContext } from "../../../Context";
import { useContext } from "react";
import Modal from "../../Modal/Modal";
import NewPostForm from "../../Forms/NewPostForm/NewPostForm";
import { useNavigate } from "react-router-dom";

export default function RegistredUserBlock() {
  const [userId, userName] = useContext(AuthContext);
  const [isModalOpen, setModalOpen] = React.useState(false);
  const navigate = useNavigate();

  const closeModal = () => {
    setModalOpen(false);
  };

  return (
    <section className="header-button-container">
      <h3>{userName}</h3>
      <Button
        className="header-button-new-post"
        onClick={() => {
          setModalOpen(true);
        }}
      >
        New post
      </Button>
      <Button
        className="header-button-profile"
        onClick={() => {
          navigate("/profile");
        }}
      >
        Profile
      </Button>
      <Button
        className="header-button-logout"
        onClick={() => {
          Logout().then(() => window.location.reload());
        }}
      >
        Выйти
      </Button>
      <Modal open={isModalOpen}>
        <div className="modal-content">
          <NewPostForm closeModal={closeModal} />
        </div>
      </Modal>
    </section>
  );
}
